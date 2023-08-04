from django.forms import ModelForm

from app.models import Accommodation

class AccommodationForm (ModelForm) :

    class Meta :
        model = Accommodation
        fields = '__all__'