from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.


def contact_us(request):
    """ A view to return the contact us page """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
        try:
            send_mail(subject, message, "donotreply@georgeshawbrewery.com", ['donotreply@georgeshawbrewery.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect("contact/thankyou.html")
    else:
        form = ContactForm()
        context = {
            'form': form,
        }

    return render(request, 'contact/contact-us.html', context)
