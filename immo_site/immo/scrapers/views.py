from django.shortcuts import render

from . my_scrapers.immoweb import scrape_overview_page, scrape__detail_page
from .my_scrapers.catfacts import get_cat_fact
from .models import ImmoWebData

from django.db import IntegrityError 
# Create your views here.

def overview(request):
    template_name = "scrapers/overview.html"
    return render(request, template_name=template_name)


def scrape_immoweb(request):
    template_name = "scrapers/scrape_immoweb.html" 

    if request.method == 'POST':
        postal_code = request.POST['postal_code']
        url = f"https://www.immoweb.be/nl/zoeken/huis/te-koop/locatie/{postal_code}?&page=1"
        all_urls = scrape_overview_page(url=url)
        for url in all_urls:
            id = url.split('/')[-1]
            obj, created = ImmoWebData.objects.get_or_create(original_url=url, original_id=id, postal_code=postal_code)
            if created:
                data = scrape__detail_page(url)
                price = data['av_items']['price']
                obj.price=price
                obj.save()
            # print(obj, ' : ', created)
        

    return render(request, template_name=template_name)

def show_original_urls(request):
    template_name = "scrapers/show_original_urls.html" 

    original_urls = ImmoWebData.objects.all()

    context = {
        'original_urls' : original_urls
    }

    return render(request, template_name=template_name, context=context)


def show_cat_facts(request):
    template_name = "scrapers/cat_facts.html" 
    print(request.POST)
    cat_fact= ""
    if request.method == 'POST':
        if request.POST['new_fact'] == 'catfact':
            cat_fact = get_cat_fact()
    
    
    context = {
        'cat_fact' : cat_fact
    }

    return render(request, template_name=template_name, context=context)