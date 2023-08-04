from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from app.forms import LocationForm
from app.models import Location

def index(request) :
    page_title = 'Liste des emplacements'
    template = 'app/settings/location/index.html'
    location_list = Location.objects.all()
    context = {
            'page_title' : page_title,
            'location_list':location_list
        }

    return render(
        request,
        template_name=template,
        context=context  
    )

def add_location(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une localisation'
    
    if request.method == 'GET' :
        form = LocationForm()
    
    template = 'app/settings/location/add.html'
    context = {
            'page_title' : page_title,
            'form':form
        }

    return render(
        request,
        template_name=template,
        context=context  
    )

def store_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La localisation a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/location')

def edit_location(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la localisation'
    if request.method == 'GET':
        if id == 0:
            form = LocationForm()
        else:
            location = Location.objects.get(pk=id)
            form = LocationForm(instance=location)
        
        template = 'app/settings/location/edit.html'
        context = {
            'page_title' : page_title,
            'form':form
        }

        return render(
            request,
            template_name=template,
            context=context  
    )

def update_location(request, id):
    if request.method == 'POST':
        if id == 0:
            form = LocationForm(request.POST)
        else:
            location = Location.objects.get(pk=id)
            form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
        messages.success(request, "La localisation a été modifié avec succès !")
        return redirect('/location')
    
def delete_location(request, id) :
    location = Location.objects.get(pk = id)
    location.delete()
    messages.success(request,"La localisation a été supprimé avec succès !")
    return redirect('/location')
