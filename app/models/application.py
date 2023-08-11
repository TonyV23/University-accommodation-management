from django.db import models
from app.models import Student, Accommodation
from django.contrib.auth.models import User

class Application(models.Model) :
       
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, null=True)
    residence_card_number = models.CharField(max_length=20)
    application_letter = models.TextField(max_length=500)
    date_application = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.student.last_name+ " - "+self.student.first_name

    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['student','accommodation','residence_card_number', 'application_letter', 'date_application'],
                name = 'unique_bedroom_application'
            )
        ]