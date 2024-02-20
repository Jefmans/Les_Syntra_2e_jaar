from django.shortcuts import render, redirect

from .forms import MyDataForm
from .models import MyData

# Create your views here.
def ___(request):
    template_name = "photo_docs/____.html"

    context = {

    }
    
    return render(request, context=context, template_name=template_name)

def show_images(request):
    template_name = "photo_docs/show_images.html"

    all_images = MyData.objects.all()

    context = {
        'images' : all_images,
    }
    
    return render(request, context=context, template_name=template_name)


def overview(request):
    template_name = "photo_docs/overview.html"

    context = {

    }
    
    return render(request, context=context, template_name=template_name)



def upload_image(request):    
    template_name = "photo_docs/upload_image.html"

    if request.method == 'POST':
        
        form = MyDataForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('docs:overview')
    else:
        form = MyDataForm()

    context = {
        'form' : form,
    }

    return render(request, context=context, template_name=template_name)


