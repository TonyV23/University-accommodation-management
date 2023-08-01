from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest

from app.forms import FacultyForm
from app.models import Faculty

def index(request) :
    page_title = 'Liste des facultés'
    template = 'app/settings/faculty/index.html'
    faculties_list = Faculty.objects.all()
    context = {
            'page_title' : page_title,
            'faculties_list':faculties_list
        }

    return render(
        request,
        template_name=template,
        context=context  
    )

def add_faculty(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter une faculté'
    
    if request.method == 'GET' :
        form = FacultyForm()
    
    template = 'app/settings/faculty/add.html'
    context = {
            'page_title' : page_title,
            'form':form
        }

    return render(
        request,
        template_name=template,
        context=context  
    )

def store_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La faculté a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/settings/faculty/index')

def edit_faculty(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier la faculté'
    if request.method == 'GET':
        if id == 0:
            form = FacultyForm()
        else:
            faculty = Faculty.objects.get(pk=id)
            form = FacultyForm(instance=faculty)
        
        template = 'app/settings/faculty/edit.html'
        context = {
            'page_title' : page_title,
            'form':form
        }

        return render(
            request,
            template_name=template,
            context=context  
    )

def update_faculty (request, id):
    if request.method == 'POST':
        if id == 0:
            form = FacultyForm(request.POST)
        else:
            faculty = Faculty.objects.get(pk=id)
            form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
        messages.success(request, "La faculté a été modifié avec succès !")
        return redirect('/settings/faculty/index')
    
def delete_faculty (request, id) :
    faculty = Faculty.objects.get(pk = id)
    faculty.delete()
    messages.success(request,"La faculté a été supprimé avec succès !")
    return redirect('/settings/faculty/index')
