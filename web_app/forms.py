from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, label='Your Email Address')
