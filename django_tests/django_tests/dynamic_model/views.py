from django.shortcuts import render
from .models import Blog

# Create your views here.


def test(request):
    template_name = "dynamic_model/test.html"
    # all_tr = soup.find_all()


    names = {'naam' : ['Naam:', 'Name:', ]}

    # blog_data = {}
    for tr in all_tr:
        if tr.split(':')[0] in names['naam']:
            "blog_data['naam'] = 'value'"

    # for tr in all_tr:
    #     for word in names['naam']:
    #         if word in tr:
    #             'do iest'


    blog_data = {
        "name": "Cheddar Talk",
        "tagline": "Thoughts on cheese."
    }

    b2 = Blog()
    for key, value in blog_data.items():
        setattr(b2, key, value)
    print(b2.name)
    
    b2.save()



    context = {
    }
    return render(request, context=context, template_name=template_name)    