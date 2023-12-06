from django.shortcuts import render

# Create your views here.


def home(request):
    template_name = "main/home.html" 

    return render(request, template_name=template_name)

