from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients =['ed@velabri.co']

            send_mail(contact_name, message, email, recipients)
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form,})