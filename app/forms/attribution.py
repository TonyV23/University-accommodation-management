from django.forms import ModelForm

from app.models import Attribution

class AttributionForm (ModelForm) :

    class Meta :
        model = Attribution
        fields = '__all__'