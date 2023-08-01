from django.db import models
from app.models import Student

class Attribution(models.Model) :
       
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    application_letter = models.TextField(max_length=500)
    date_application = models.DateField()
    
    def __str__(self) -> str:
        return self.designation
    
    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['student', 'application_letter', 'date_application'],
                name = 'unique_attribution'
            )
        ]