# forms.py

from django import forms

class BookForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.HiddenInput())