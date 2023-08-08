from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.forms import DepartmentForm
from app.models import Faculty
from app.models import Department

@login_required(login_url ='login')
def index(request):
    page_title = 'Liste des departments'
    departments_list = Department.objects.all()
    template = 'app/settings/department/index.html'
    context = {
        'page_title' : page_title,
        'departments_list' : departments_list
    }

    return render(
        request,
        template_name=template,
        context=context  
    )

@login_required(login_url ='login')
def add_department(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter un department'
    faculties = Faculty.objects.all()

    if request.method == 'GET' :
        form = DepartmentForm()
    template = 'app/settings/department/add.html'
    context =  {
        'form' : form,
        'page_title' : page_title,
        'faculties' : faculties
    }

    return render(
        request,
        template_name=template,
        context=context  
    )

@login_required(login_url ='login')
def store_department(request):
    if request.method == 'POST':
        form =  DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le department a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/department')

@login_required(login_url ='login')
def edit_department(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Modifier le department'
    if request.method == 'GET':
        if id == 0:
            form = DepartmentForm()
        else:
            faculty = Department.objects.get(pk=id)
            form = DepartmentForm(instance=faculty)
        
        template = 'app/settings/department/edit.html'
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
def update_department(request, id):
    if request.method == 'POST':
        if id == 0:
            form = DepartmentForm(request.POST)
        else:
            department = Department.objects.get(pk=id)
            form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
        messages.success(request, "Le department a été modifié avec succès !")
        return redirect('/department')

@login_required(login_url ='login')    
def delete_department(request, id) :
    department = Department.objects.get(pk = id)
    department.delete()
    messages.success(request,"Le department a été supprimé avec succès !")
    return redirect('/department')


