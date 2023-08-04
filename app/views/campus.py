from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from app.forms import CampusForm
from app.models import Campus

def index(request) :
    page_title = 'Liste des campus'
    template = 'app/settings/campus/index.html'
    campus_list = Campus.objects.all()
    context = {
            'page_title' : page_title,
            'campus_list':campus_list
        }

    return render(
        request,
        template_name=template,
        context=context  
    )

def add_campus(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter un campus'
    
    if request.method == 'GET' :
        form = CampusForm()
    
    template = 'app/settings/campus/add.html'
    context = {
            'page_title' : page_title,
            'form':form
        }

    return render(
        request,
        template_name=template,
        context=context  
    )

def store_campus(request):
    if request.method == 'POST':
        form = CampusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le campus a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/settings/campus/index')

def edit_campus(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier le campus'
    if request.method == 'GET':
        if id == 0:
            form = CampusForm()
        else:
            campus = Campus.objects.get(pk=id)
            form = CampusForm(instance=campus)
        
        template = 'app/settings/campus/edit.html'
        context = {
            'page_title' : page_title,
            'form':form
        }

        return render(
            request,
            template_name=template,
            context=context  
    )

def update_campus(request, id):
    if request.method == 'POST':
        if id == 0:
            form = CampusForm(request.POST)
        else:
            campus = Campus.objects.get(pk=id)
            form = CampusForm(request.POST, instance=campus)
        if form.is_valid():
            form.save()
        messages.success(request, "Le campus a été modifié avec succès !")
        return redirect('/settings/campus/index')
    
def delete_campus(request, id) :
    campus = Campus.objects.get(pk = id)
    campus.delete()
    messages.success(request,"Le campus a été supprimé avec succès !")
    return redirect('/settings/campus/index')