from django.db import models
from app.models import Student

class Application(models.Model) :
       
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    application_letter = models.TextField(max_length=500)
    date_application = models.DateField(auto_now_add=True)

    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['student', 'application_letter', 'date_application'],
                name = 'unique_bedroom_application'
            )
        ]