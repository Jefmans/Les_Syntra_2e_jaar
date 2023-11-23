from django.shortcuts import render

from . my_scrapers.immoweb import scrape_overview_page

from .models import ImmoWebData

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
            immo_object = ImmoWebData(original_url=url)
            immo_object.save()



    return render(request, template_name=template_name)

def show_original_urls(request):
    template_name = "scrapers/show_original_urls.html" 

    original_urls = ...

    context = {
        'original_urls' : original_urls
    }

    return render(request, template_name=template_name, context=context)