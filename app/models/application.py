from django.db import models
from app.models import Student, Accommodation

class Application(models.Model) :
       
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    residence_card_number = models.CharField(max_length=20)
    application_letter = models.TextField(max_length=500)
    date_application = models.DateField(auto_now_add=True)

    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['student','accommodation','residence_card_number', 'application_letter', 'date_application'],
                name = 'unique_bedroom_application'
            )
        ]