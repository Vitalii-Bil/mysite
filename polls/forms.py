from django import forms


class TriangleForm(forms.Form):
	leg1 = forms.FloatField(required=True, min_value=0.0)
	leg2 = forms.FloatField(required=True, min_value=0.0)
