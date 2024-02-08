from django.shortcuts import render
from .mails import send_test
from django.http import HttpResponse

from django.contrib import messages


# Create your views here.

def ___(request):
    template_name = "photo_docs/____.html"

    context = {

    }
    
    return render(request, context=context, template_name=template_name)

def send_mail(request):
    template_name = "emailing/send_mail.html"
    context = {}

    if request.method == 'POST':
        # email_to = request.user.email
        email_to = "jefvanrompay@yahoo.co.uk"
        username = "jefmans"
        send_test(request, username, email_to)

        messages.success(request, 'Your email has been send')

        return render(request, context=context, template_name=template_name)
    
    
    return render(request, context=context, template_name=template_name)




