from django.forms import ModelForm

from app.models import Application

class RefugeeForm (ModelForm) :

    class Meta :
        model = Application
        fields = '__all__'