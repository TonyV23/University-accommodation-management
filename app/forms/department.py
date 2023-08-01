from django.forms import ModelForm

from app.models import Department

class RefugeeForm (ModelForm) :

    class Meta :
        model = Department
        fields = '__all__'