from django.shortcuts import render, get_object_or_404, redirect
from .models import Dier, Soort, Kleur

# Create your views here.

def dier_list(request):
    dieren_all = Dier.objects.all()
    template_name = "dieren/dier_list.html"
    context = {
        "dieren" : dieren_all,
    }
    return render(request, template_name=template_name, context=context)

def dier_detail(request, dier_id):
    dier = get_object_or_404(Dier, id=dier_id)
    template_name = "dieren/dier_detail.html"
    context = {
        "dier" : dier,
    }
    return render(request, template_name=template_name, context=context)

def dier_create(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        dier_naam = request.POST['naam']
        dier_kleur_id = request.POST['kleur']
        dier_kleur = Kleur.objects.get(id=dier_kleur_id)
        dier_soort_value = request.POST['soort']
        dier_soort = Soort.objects.get(id=dier_soort_value)
        dier_grootte = request.POST['grootte']
        new_dier = Dier(naam= dier_naam, kleur=dier_kleur , grootte=dier_grootte , soort=dier_soort)
        new_dier.save()
        return redirect("dieren:dier_list")
    else:
        soorten = Soort.objects.all()
        kleuren = Kleur.objects.all()
        template_name = "dieren/dier_create.html"
        context = {
            "soorten": soorten,
            "kleuren": kleuren,
        }
        return render(request, template_name=template_name, context=context)