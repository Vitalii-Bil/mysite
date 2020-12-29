from django import forms

from .models import Person


class TriangleForm(forms.Form):
    leg1 = forms.FloatField(required=True, min_value=0.0)
    leg2 = forms.FloatField(required=True, min_value=0.0)


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
