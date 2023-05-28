from django.shortcuts import render, HttpResponseRedirect
from .forms import LivreForm
from . import models


def index(request):
    liste = list(models.Livre.objects.all())
    return render(request,'bibliotheque/index.html',{"liste":liste})


def ajout(request):
    form = LivreForm() # création d'un formulaire vide
    return render(request,"bibliotheque/ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"bibliotheque/affiche.html",{"livre" : livre})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})
    
def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request, "bibliotheque/affiche.html", {'livre':livre})

def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/bibliotheque/")

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False) # création d'un objet Livre avec les données du formulaire mais sans l'enregistrer dans la base.
        Livre.id = id; # modification de l'id de l'objet
        Livre.save() # mise à jour dans la base puisque l'id du Livre existe déja.
        return HttpResponseRedirect("/bibliotheque/") # plutot que d'avoir un gabarit pour nous indiquer que cela c'est bien passé, nous repartons sur une autre action qui renvoie vers la page d'index de notre site (celle avec la liste des entrées)
    else:
        return render(request, "bibliotheque/update.html", {"form": lform, "id": id})

def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    lform = LivreForm(livre.__dict__)
    return render(request, "bibliotheque/update.html", {"form":lform, "id":id})