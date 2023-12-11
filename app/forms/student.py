from django.forms import ModelForm
from django import forms

from app.models import Student

class StudentForm (ModelForm) :

    class Meta :
        model = Student
        exclude =['matricule']
        widgets = {
            "birth_date": forms.TextInput(attrs={'type': 'date'})
        }