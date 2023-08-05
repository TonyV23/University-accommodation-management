from django.shortcuts import render
from app.models import Student, BedRoom, Application, Attribution


def index(request) :
    
    page_title = 'Tableau de Bord'
    template = 'app/home/index.html'

    all_students = Student.objects.all().count()
    all_bedrooms = BedRoom.objects.all().count()
    all_applications = Application.objects.all().count()
    all_attributions = Attribution.objects.all().count()

    context = {
            'page_title' : page_title,
            'all_students' : all_students,
            'all_bedrooms' : all_bedrooms,
            'all_applications' : all_applications,
            'all_attributions' : all_attributions,
        }

    return render(
        request,
        template_name = template,
        context = context
    )