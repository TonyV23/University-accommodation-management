from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from app.forms import AccommodationForm
from app.models import Accommodation

def index(request) :
    page_title = 'Liste des types de logements'
    template = 'app/settings/accommodation/index.html'
    accommodations_list = Accommodation.objects.all()
    context = {
            'page_title' : page_title,
            'accommodations_list':accommodations_list
        }

    return render(
        request,
        template_name=template,
        context=context  
    )

def add_accommodation(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter un type de logement'
    
    if request.method == 'GET' :
        form = AccommodationForm()
    
    template = 'app/settings/accommodation/add.html'
    context = {
            'page_title' : page_title,
            'form':form
        }

    return render(
        request,
        template_name=template,
        context=context  
    )

def store_accommodation(request):
    if request.method == 'POST':
        form = AccommodationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le type de logement a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/settings/accommodation/index')

def edit_accommodation(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier le type de logement'
    if request.method == 'GET':
        if id == 0:
            form = AccommodationForm()
        else:
            accommodation = Accommodation.objects.get(pk=id)
            form = AccommodationForm(instance=accommodation)
        
        template = 'app/settings/accommodation/edit.html'
        context = {
            'page_title' : page_title,
            'form':form
        }

        return render(
            request,
            template_name=template,
            context=context  
    )

def update_accommodation(request, id):
    if request.method == 'POST':
        if id == 0:
            form = AccommodationForm(request.POST)
        else:
            accommodation = Accommodation.objects.get(pk=id)
            form = AccommodationForm(request.POST, instance=accommodation)
        if form.is_valid():
            form.save()
        messages.success(request, "Le type de logement a été modifié avec succès !")
        return redirect('/settings/accommodation/index')
    
def delete_accommodation(request, id) :
    accommodation = Accommodation.objects.get(pk = id)
    accommodation.delete()
    messages.success(request,"Le type de logement a été supprimé avec succès !")
    return redirect('/settings/accommodation/index')
