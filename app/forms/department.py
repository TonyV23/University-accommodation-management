from django.forms import ModelForm

from app.models import Department

class DepartmentForm (ModelForm) :

    class Meta :
        model = Department
        fields = '__all__'