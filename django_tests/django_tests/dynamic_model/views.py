from django.shortcuts import render
from .models import Blog

# Create your views here.


def test(request):
    template_name = "dynamic_model/test.html"
    
    names = {'naam' : ['Naam:', 'Name:', ]}

    blog_data = {
        "name": "Cheddar Talk",
        "tagline": "Thoughts on cheese."
    }
    blog_data['Ondernemingsnummer'] = tr.text

    b2 = Blog()
    for key, value in blog_data.items():
        setattr(b2, key, value)
    print(b2.name)
    
    b2.save()

    context = {
    }
    return render(request, context=context, template_name=template_name)    