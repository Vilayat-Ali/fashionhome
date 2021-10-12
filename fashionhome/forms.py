from django import forms

class contactForm(forms.Form):
    name = forms.CharField(max_length=155)
    email = forms.EmailField(max_length=300)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(max_length=500)
    