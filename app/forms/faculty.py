from django.forms import ModelForm

from app.models import Faculty

class RefugeeForm (ModelForm) :

    class Meta :
        model = Faculty
        fields = '__all__'