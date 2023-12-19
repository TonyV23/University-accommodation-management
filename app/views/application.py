from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.forms import ApplicationForm, ApplicationStatusForm
from app.models import Application, Student
from app.decorators import allowed_users


@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins'])
def index(request) :
    page_title = 'Liste des demandes'
    template = 'app/settings/application/index.html'
    application_list = Application.objects.filter(status=2)
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
@allowed_users(allowed_roles= ['students'])
def index_student(request) :
    page_title = 'Liste des demandes'
    template = 'app/settings/application/index_student.html'
    application_list = Application.objects.filter(created_by=request.user)
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
@allowed_users(allowed_roles= ['admins'])
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
@allowed_users(allowed_roles= ['students'])
def add_application_student(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Faire une demande'
    
    if request.method == 'GET' :
        form = ApplicationForm()
    
    template = 'app/settings/application/add_student.html'
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
@allowed_users(allowed_roles= ['admins', 'students'])
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
@allowed_users(allowed_roles= ['students'])
def store_application_student(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.created_by = request.user
            student_matricule = form.cleaned_data.get('matricule')
            try:
                student = Student.objects.get(matricule=student_matricule)
                if student.matricule == application.matricule:
                    application.save()
                    messages.success(request, "Votre demande a été envoyée avec succès!")
                else:
                    messages.error(request, "Le matricule ne correspond pas.")
            except Student.DoesNotExist:
                messages.error(request, "Étudiant introuvable.")
        else:
            messages.error(request, form.errors)

        return redirect('/applicationStudent')

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['admins', 'students'])
def edit_application(request, id):
    assert isinstance(request, HttpRequest)
    page_title = "Visualiser la demande "
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
@allowed_users(allowed_roles= ['students'])
def edit_application_student(request, id):
    assert isinstance(request, HttpRequest)
    page_title = "Modifier la demande "
    if request.method == 'GET':
        if id == 0:
            form = ApplicationForm()
        else:
            application = Application.objects.get(pk=id)
            form = ApplicationForm(instance=application)
        
        template = 'app/settings/application/edit_student.html'
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
@allowed_users(allowed_roles= ['admins', 'students'])
def update_application(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ApplicationForm(request.POST)
        else:
            application = Application.objects.get(pk=id)
            form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
        # messages.success(request, "La demande a été modifié avec succès !")
        return redirect('/application')
    
@login_required(login_url ='login')
@allowed_users(allowed_roles= ['students'])
def update_application_student(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ApplicationForm(request.POST)
        else:
            application = Application.objects.get(pk=id)
            form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
        messages.success(request, "La demande a été modifié avec succès !")
        return redirect('/applicationStudent')
    
@login_required(login_url ='login')    
@allowed_users(allowed_roles= ['admins', 'students'])
def delete_application(request, id) :
    application = Application.objects.get(pk = id)
    application.delete()
    messages.success(request,"La demande a été supprimé avec succès !")
    return redirect('/application')


@login_required(login_url ='login')    
@allowed_users(allowed_roles= ['students'])
def delete_application_student(request, id) :
    application = Application.objects.get(pk = id)
    application.delete()
    messages.success(request,"La demande a été supprimé avec succès !")
    return redirect('/applicationStudent')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'students'])
def edit_application_status(request, id):
    assert isinstance(request, HttpRequest)
    page_title = "Modifier le statut de la demande"
    if request.method == 'GET':
        application = Application.objects.get(pk=id)
        form = ApplicationStatusForm(instance=application)
        template = 'app/settings/application/edit_status.html'
        context = {
            'page_title': page_title,
            'form': form
        }
        return render(request, template_name=template, context=context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins', 'students'])
def update_application_status(request, id):
    if request.method == 'POST':
        if id == 0:
            form = ApplicationForm(request.POST)
        else:
            application = Application.objects.get(pk=id)
            form = ApplicationStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le statut de la demande a été mis à jour avec succès.')
            return redirect('/application')
        else:
            print(form.errors)
            messages.error(request, 'Une erreur s\'est produite lors de la mise à jour du statut de la demande.')
            return redirect('/application')