from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

from app.forms import StudentForm
from app.models import Student, Faculty, Department

@login_required(login_url ='login')
def index(request):
    page_title = 'Liste des etudiants'
    students_list = Student.objects.all()
    template = 'app/settings/student/index.html'
    context = {
        'page_title' : page_title,
        'students_list' : students_list
    }

    return render(
        request,
        template_name=template,
        context=context  
    )

@login_required(login_url ='login')
def add_student(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Ajouter un etudiant'
    faculties = Faculty.objects.all()
    departments = Department.objects.all()

    if request.method == 'GET' :
        form = StudentForm()
    template = 'app/settings/student/add.html'
    context =  {
        'form' : form,
        'page_title' : page_title,
        'faculties' : faculties,
        'departments' : departments
    }

    return render(
        request,
        template_name=template,
        context=context  
    )

@login_required(login_url ='login')
def store_student(request):
    if request.method == 'POST':
        form =  StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"L' etudiant a été enregistré avec succès !")
        else :
            messages.error(request, form.errors)
        return redirect('/student')

@login_required(login_url ='login')
def edit_student(request, id):
    assert isinstance(request, HttpRequest)
    page_title = "Modifier l' etudiant"
    if request.method == 'GET':
        if id == 0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)
        
        template = 'app/settings/student/edit.html'
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
def update_student(request, id):
    if request.method == 'POST':
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        messages.success(request, "L' etudiant a été modifié avec succès !")
        return redirect('/student')

@login_required(login_url ='login')    
def delete_student(request, id) :
    student = Student.objects.get(pk = id)
    student.delete()
    messages.success(request,"L'etudiant a été supprimé avec succès !")
    return redirect('/student')


