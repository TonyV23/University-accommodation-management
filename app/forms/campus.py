from django.forms import ModelForm

from app.models import Campus

class CampusForm (ModelForm) :

    class Meta :
        model = Campus
        fields = '__all__'