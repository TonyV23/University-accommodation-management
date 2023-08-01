from django.forms import ModelForm

from app.models import Student

class RefugeeForm (ModelForm) :

    class Meta :
        model = Student
        fields = '__all__'