from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label='Name', max_length=80)
    email = forms.EmailField(required=True, label='Email')
    message = forms.CharField(required=True, label='Your Message', widget=forms.Textarea)

