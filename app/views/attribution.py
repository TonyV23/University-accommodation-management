from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.forms import AttributionForm
from app.models import Application, Student, BedRoom
from app.decorators import allowed_users

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def index(request):
    page_title = 'Liste des attributions des chambres'
    attribution_list = Application.objects.filter(status=1)
    template = 'app/settings/attribution/index.html'
    context = {
        'page_title' : page_title,
        'attribution_list' : attribution_list
    }

    return render(
        request,
        template_name=template,
        context=context  
    )

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def add_attribution(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Faire une attribution'
    students = Student.objects.all()
    bedrooms = BedRoom.objects.all()

    if request.method == 'GET' :
        form = AttributionForm()
    template = 'app/settings/attribution/add.html'
    context =  {
        'form' : form,
        'page_title' : page_title,
        'students' : students,
        'bedrooms' : bedrooms
    }

    return render(
        request,
        template_name=template,
        context=context  
    )

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def store_attribution(request):
    if request.method == 'POST':
        form =  AttributionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"L'attribution a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/attribution')

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def edit_attribution(request, id):
    assert isinstance(request, HttpRequest)
    page_title = "Modifier l'attribution"
    if request.method == 'GET':
        if id == 0:
            form = AttributionForm()
        else:
            attribution = Attribution.objects.get(pk=id)
            form = AttributionForm(instance=attribution)
        
        template = 'app/settings/attribution/edit.html'
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
def update_attribution(request, id):
    if request.method == 'POST':
        if id == 0:
            form = AttributionForm(request.POST)
        else:
            attribution = Attribution.objects.get(pk=id)
            form = AttributionForm(request.POST, instance=attribution)
        if form.is_valid():
            form.save()
        messages.success(request, "L'attribution a été modifié avec succès !")
        return redirect('/attribution')

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])    
def delete_attribution(request, id) :
    attribution = Attribution.objects.get(pk = id)
    attribution.delete()
    messages.success(request,"L'attribution a été supprimé avec succès !")
    return redirect('/attribution')

    
