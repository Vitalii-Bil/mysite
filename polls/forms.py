import datetime

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Person


class TriangleForm(forms.Form):
    leg1 = forms.FloatField(required=True, min_value=0.0)
    leg2 = forms.FloatField(required=True, min_value=0.0)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']


class ReminderForm(forms.Form):
    email = forms.EmailField(required=True, max_length=254)
    text = forms.CharField(required=True, max_length=200)
    rem_date = forms.DateTimeField(required=True, initial=datetime.datetime.now)

    def clean_date_and_time(self):
        rem_date = self.cleaned_data['rem_date']
        if rem_date < datetime.datetime.now():
            raise forms.ValidationError(_('The date must be no earlier than the current date'))
        if rem_date > datetime.datetime.now() + datetime.timedelta(days=2):
            raise forms.ValidationError(_('The date must be no later than 2 days'))

        return rem_date
