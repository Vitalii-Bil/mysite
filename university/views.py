from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Student, University


@method_decorator(cache_page(10), name='dispatch')
class StudentList(ListView):
    model = Student
    paginate_by = 10
    template_name = 'university/student_list_page.html'
    ordering = ['first_name', 'last_name']


@method_decorator(cache_page(10), name='dispatch')
class StudentDetail(DetailView):
    model = Student
    template_name = 'university/student_detail_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StudentCreate(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'date_of_birth', 'university', 'lecturer']
    template_name = 'university/student_create_page.html'
    success_url = reverse_lazy('university:student_list')


class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ['first_name', 'last_name', 'date_of_birth', 'university', 'lecturer']
    template_name = 'university/student_update_page.html'

    def get_success_url(self):
        studentid = self.kwargs['pk']
        return reverse_lazy('university:student_detail', kwargs={'pk': studentid})


class StudentDelete(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('university:student_list')
    template_name = 'university/student_delete_page.html'


@method_decorator(cache_page(10), name='dispatch')
class UniversityList(ListView):
    model = University
    paginate_by = 10
    template_name = 'university/university_list_page.html'
    queryset = University.objects.all().prefetch_related('student_set').all()
    ordering = ['name']
