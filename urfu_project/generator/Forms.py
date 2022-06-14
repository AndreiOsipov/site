from attr import attr, attrs
from django import forms

class KeyWordForm(forms.Form):
    word = forms.CharField(
        required = False, 
        max_length=100, 
        label='', 
        label_suffix='',
        widget=forms.TextInput(attrs={"class": "input_field"}))