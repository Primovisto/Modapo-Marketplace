from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(contact_name, email, message, ['testing@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "contact/contact.html", {'form': form})


def thanks(request):
    return render(request, 'contact/thanks_message.html')
