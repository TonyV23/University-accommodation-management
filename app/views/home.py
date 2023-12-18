from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from app.models import Student, BedRoom, Application, Attribution
from app.decorators import admin_only, allowed_users


@login_required(login_url ='login')
@admin_only
def index(request) :
    
    page_title = 'Accueil |Tableau de Bord'
    template = 'app/home/index.html'

    all_students = Student.objects.all().count()
    all_bedrooms = BedRoom.objects.all().count()
    all_applications = Application.objects.filter(status=2).count()
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

@login_required(login_url ='login')
@allowed_users(allowed_roles= ['students'])
def index_student(request):
    page_title = 'Accueil'
    template = 'app/home/index_student.html'

    applications = Application.objects.filter(created_by=request.user)
    application_list = Application.objects.filter(created_by=request.user)

    attribution_list = []
    for application in applications:
        attribution = Attribution.objects.filter(student=application).first()
        if attribution:
            attribution_list.append(attribution)

    context = {
        'page_title': page_title,
        'applications': applications,
        'application_list': application_list,
        'attributions': attribution_list,
    }

    return render(
        request,
        template_name=template,
        context=context
    )