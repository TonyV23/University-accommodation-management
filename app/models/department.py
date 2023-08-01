from django.db import models
from app.models import Faculty

class Department(models.Model) :
    designation = models.CharField(max_length=20)
    faculty_name = models.ForeignKey(Faculty, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.designation
    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['designation', 'faculty_name'],
                name = 'unique_department'
            )
        ]