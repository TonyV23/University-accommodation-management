from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.forms import ApplicationForm
from app.models import Application


@login_required(login_url ='login')
def index(request) :
    page_title = 'Liste des demandes'
    template = 'app/settings/application/index.html'
    application_list = Application.objects.all()
    context = {
            'page_title' : page_title,
            'application_list':application_list
        }

    return render(
        request,
        template_name=template,
        context=context  
    )

@login_required(login_url ='login')
def add_application(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Faire une demande'
    
    if request.method == 'GET' :
        form = ApplicationForm()
    
    template = 'app/settings/application/add.html'
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
def store_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"La demande a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/application')

@login_required(login_url ='login')
def edit_application(request, id):
    assert isinstance(request, HttpRequest)
    page_title = "Modifier la demande "
    if request.method == 'GET':
        if id == 0:
            form = ApplicationForm()
        else:
            application = Application.objects.get(pk=id)
            form = ApplicationForm(instance=application)
        
        template = 'app/settings/application/edit.html'
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
def update_application(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ApplicationForm(request.POST)
        else:
            application = Application.objects.get(pk=id)
            form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
        messages.success(request, "La demande a été modifié avec succès !")
        return redirect('/application')
    
@login_required(login_url ='login')    
def delete_application(request, id) :
    application = Application.objects.get(pk = id)
    application.delete()
    messages.success(request,"La demande a été supprimé avec succès !")
    return redirect('/application')
