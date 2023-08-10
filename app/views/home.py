from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from app.models import Student, BedRoom, Application, Attribution
from app.decorators import admin_only


@login_required(login_url ='login')
@admin_only
def index(request) :
    
    page_title = 'Tableau de Bord'
    template = 'app/home/index.html'

    all_students = Student.objects.all().count()
    all_bedrooms = BedRoom.objects.all().count()
    all_applications = Application.objects.all().count()
    all_attributions = Attribution.objects.all().count()

    true_bedrooms = BedRoom.objects.filter(status=True).count()
    false_bedrooms = BedRoom.objects.filter(status=False).count()

    context = {
            'page_title' : page_title,
            'all_students' : all_students,
            'all_bedrooms' : all_bedrooms,
            'all_applications' : all_applications,
            'all_attributions' : all_attributions,
            'true_bedrooms' : true_bedrooms,
            'false_bedrooms' : false_bedrooms
        }

    return render(
        request,
        template_name = template,
        context = context
    )

def index_student(request) :
    page_title = 'Accueil'
    template = 'app/home/index_student.html'
    context = {
        'page_title' : page_title,
    }

    return render(
        request,
        template_name=template,
        context=context
    )