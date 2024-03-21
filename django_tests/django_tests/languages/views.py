from django.shortcuts import render

# Create your views here.


def show_language(request):
    template_name = "languages/show_language.html"

    context = {

    }
    
    return render(request, context=context, template_name=template_name)




def settings_language(request):
    template_name = "languages/set_language.html"

    context = {

    }
    
    return render(request, context=context, template_name=template_name)