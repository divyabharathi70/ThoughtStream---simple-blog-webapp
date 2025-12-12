from django import forms

class Contact (forms.Form):
    name = forms.CharField(label='Name',max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message',max_length=100)