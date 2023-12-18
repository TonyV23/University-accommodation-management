from django.forms import ModelForm
from django import forms

from app.models import Application

class ApplicationForm (ModelForm) :

    class Meta :
        model = Application
        exclude = ['status','created_by']
        widgets = {
            "entry_date": forms.TextInput(attrs={'type': 'date'})
        }

class ApplicationStatusForm (forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status']