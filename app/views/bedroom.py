from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.forms import BedroomForm
from app.models import Location
from app.models import BedRoom
from app.decorators import allowed_users

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def index(request):
    page_title = 'Liste des chambres'
    bedrooms_list = BedRoom.objects.all()
    template = 'app/settings/bedroom/index.html'
    context = {
        'page_title' : page_title,
        'bedrooms_list' : bedrooms_list
    }

    return render(
        request,
        template_name=template,
        context=context  
    )

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def add_bedroom(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une chambre'
    locations = Location.objects.all()

    if request.method == 'GET' :
        form = BedroomForm()
    template = 'app/settings/bedroom/add.html'
    context =  {
        'form' : form,
        'page_title' : page_title,
        'locations' : locations
    }

    return render(
        request,
        template_name=template,
        context=context  
    )

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def store_bedroom(request):
    if request.method == 'POST':
        form =  BedroomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La chambre a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/bedroom')

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def edit_bedroom(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la chambre'
    if request.method == 'GET':
        if id == 0:
            form = BedroomForm()
        else:
            location = BedRoom.objects.get(pk=id)
            form = BedroomForm(instance=location)
        
        template = 'app/settings/bedroom/edit.html'
        context = {
            'page_title' : page_title,
            'form':form
        }

        return render(
            request,
            template_name=template,
            context=context  
    )

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def update_bedroom(request, id):
    if request.method == 'POST':
        if id == 0:
            form = BedroomForm(request.POST)
        else:
            bedroom = BedRoom.objects.get(pk=id)
            form = BedroomForm(request.POST, instance=bedroom)
        if form.is_valid():
            form.save()
        messages.success(request, "La chambre a été modifié avec succès !")
        return redirect('/bedroom')
    
@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])    
def delete_bedroom(request, id) :
    bedroom = BedRoom.objects.get(pk = id)
    bedroom.delete()
    messages.success(request,"La chambre a été supprimé avec succès !")
    return redirect('/bedroom')


