from django.shortcuts import render, redirect

from .forms import ImageForm, DocumentForm
from .models import Image, Document

# Create your views here.
def ___(request):
    template_name = "photo_docs/____.html"

    context = {

    }
    
    return render(request, context=context, template_name=template_name)

def show_images(request):
    template_name = "photo_docs/show_images.html"

    all_images = Image.objects.all()
    print(all_images)

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
        
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('docs:overview')
    else:
        form = ImageForm()

    context = {
        'form' : form,
    }

    return render(request, context=context, template_name=template_name)


def upload_doc(request):    
    template_name = "photo_docs/upload_doc.html"

    if request.method == 'POST':
        
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            doc = form.save(commit=False)
            doc.test = "new"
            doc.is_goed = True
            doc.save()
            return redirect('docs:overview')
    else:
        form = DocumentForm()

    context = {
        'form' : form,
    }

    return render(request, context=context, template_name=template_name)

def show_docs(request):
    template_name = "photo_docs/show_docs.html"

    all_docs = Document.objects.all()

    context = {
        'docs' : all_docs,
    }
    
    return render(request, context=context, template_name=template_name)
