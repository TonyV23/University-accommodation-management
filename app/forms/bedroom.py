from django.forms import ModelForm

from app.models import BedRoom

class RefugeeForm (ModelForm) :

    class Meta :
        model = BedRoom
        fields = '__all__'