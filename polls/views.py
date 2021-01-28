from math import sqrt


from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic


from .forms import PersonForm, ReminderForm, TriangleForm
from .models import Choice, Person, Question
from .tasks import send_mail as celery_send_mail


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions (not including those set to be
        published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def triangle_view(request):
    if request.method == "GET":
        form = TriangleForm()
    else:
        form = TriangleForm(request.POST)
        if form.is_valid():
            leg1 = form.cleaned_data['leg1']
            leg2 = form.cleaned_data['leg2']
            gip = sqrt(leg1 ** 2 + leg2 ** 2)
            return render(
                request,
                "polls/triangle_page.html",
                context={
                    "gip": gip,
                }
            )
    return render(
        request,
        "polls/triangle_page.html",
        context={
            "form": form,
        }
    )


def person_create(request):

    if request.method == 'POST':

        form = PersonForm(request.POST)

        if form.is_valid():
            person = Person()
            person.first_name = form.cleaned_data['first_name']
            person.last_name = form.cleaned_data['last_name']
            person.email = form.cleaned_data['email']
            person.save()

            return HttpResponseRedirect(reverse('polls:person-update', args=(person.id,)))

    else:
        form = PersonForm()

    context = {
        'form': form,
    }

    return render(request, 'polls/person_form.html', context)


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':

        form = PersonForm(request.POST)

        if form.is_valid():
            person.first_name = form.cleaned_data['first_name']
            person.last_name = form.cleaned_data['last_name']
            person.email = form.cleaned_data['email']
            person.save()

            return HttpResponseRedirect(reverse('polls:person-update', args=(person.id,)))

    else:
        form = PersonForm(initial={
            'first_name': person.first_name,
            'last_name': person.last_name,
            'email': person.email
        })

    context = {
        'form': form,
        'person': person,
    }

    return render(request, 'polls/person_form.html', context)


def reminder_view(request):
    if request.method == "GET":
        form = ReminderForm()
    else:
        form = ReminderForm(request.POST)
        if form.is_valid():
            subject = 'Напоминание'
            from_email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            send_date = form.cleaned_data['rem_date']
            celery_send_mail.apply_async((subject, text, from_email), eta=send_date)
            messages.add_message(request, messages.SUCCESS, 'Message sent')
            return redirect('polls:reminder')
    return render(request, "polls/reminder_page.html", context={"form": form, })
