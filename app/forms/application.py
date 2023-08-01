from django.forms import ModelForm

from app.models import Application

class ApplicationForm (ModelForm) :

    class Meta :
        model = Application
        fields = '__all__'