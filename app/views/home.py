from django.shortcuts import render


def index(request) :
    
    page_title = 'Tableau de Bord'
    template = 'app/home/index.html'
    context = {
            'page_title' : page_title
        }

    return render(
        request,
        template_name = template,
        context = context
    )