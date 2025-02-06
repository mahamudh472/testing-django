from django import forms

class CustomForms(forms.Form):
    name = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)
