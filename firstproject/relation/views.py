from django.shortcuts import render, HttpResponseRedirect
from . import models
from . import forms
def index(request):
    return render(request,'relation/index.html')

def all_voiture(request):
    liste = list(models.auto.objects.all())
    return render(request, 'relation/view_all_voiture.html',{'liste':liste})

def all_marque(request):
    liste = list(models.marque.objects.all())
    return render(request, 'relation/view_all_marque.html',{'liste':liste})

def ajout_voiture(request):
    form = forms.Auto_Form()
    return render(request, 'relation/add_form_voiture.html',{"form":form})

def ajout_marque(request):
    form = forms.Marque_Form()
    return render(request, 'relation/add_form_marque.html',{"form":form})

def traitement(request, id):
    if id ==1:
        form = forms.Auto_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/relation/voiture/")
        else:
            return render(request,"relation/add_form_voiture.html",{"form": form})
    if id == 2:
        form = forms.Marque_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/relation/marque/")
        else:
            return render(request,"relation/add_form_marque.html",{"form": form})

def delete_auto(request, id):
    auto = models.auto.objects.get(pk=id)
    auto.delete()
    return HttpResponseRedirect("/relation/voiture/")


def delete_marque(request, id):
    marque = models.marque.objects.get(pk=id)
    marque.delete()
    return HttpResponseRedirect("/relation/marque/")

def update_auto(request, id):
    form = forms.Auto_Form(request.POST)
    if form.is_valid():
        auto = form.save(commit=False)
        auto.id = id
        auto.save()
        return render(request,"relation/view_all_voiture.html")
    else:
        return render(request, 'relation/add_form_voiture.html',{"form":form, "id": id})
    
def update_marque(request, id):
    form = forms.Marque_Form(request.POST)
    if form.is_valid():
        marque = form.save(commit=False)
        marque.id = id
        marque.save()
        return render(request,"relation/view_all_marque.html")
    else:
        return render(request, 'relation/add_form_marque.html',{"form":form, "id": id})
    
def view_auto(request, id):
    auto = models.auto.objects.get(pk=id)
    return render(request, "relation/view_auto.html", {'auto':auto})

def view_marque(request, id):
    marque = models.marque.objects.get(pk=id)
    return render(request, "relation/view_marque.html", {'marque':marque})