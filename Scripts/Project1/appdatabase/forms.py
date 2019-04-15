from django import forms
from .models import Human

class HumanForm(forms.Form):
    title = forms.CharField(max_length=50)