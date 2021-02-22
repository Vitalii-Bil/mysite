from django import forms


class FeedbackFrom(forms.Form):
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
