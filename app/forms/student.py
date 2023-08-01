from django.forms import ModelForm

from app.models import Student

class StudentForm (ModelForm) :

    class Meta :
        model = Student
        fields = '__all__'