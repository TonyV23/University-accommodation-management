from django.forms import ModelForm

from app.models import Location

class RefugeeForm (ModelForm) :

    class Meta :
        model = Location
        fields = '__all__'