from django.shortcuts import render

from .forms import ContactForm
# Create your views here.

def home(request):
    template_name = "main/home.html" 

    return render(request, template_name=template_name)


def contact_us(request):
    template_name = "main/contact_us.html" 

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            message = 'thank you'
            context = {
                'message' : message
            }
            return render(request, template_name=template_name, context=context)
    else:
        form = ContactForm()


    context = {
        'form':form
    }
    return render(request, template_name=template_name, context=context)

