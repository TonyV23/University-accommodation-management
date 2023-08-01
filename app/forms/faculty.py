from django.forms import ModelForm

from app.models import Faculty

class FacultyForm (ModelForm) :

    class Meta :
        model = Faculty
        fields = '__all__'