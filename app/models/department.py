from django.db import models
from app.models import Faculty

class Department(models.Model) :
    designation = models.CharField(max_length=20)
    nom_de_la_faculte = models.ForeignKey(Faculty, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.designation
    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['designation', 'nom_de_la_faculte'],
                name = 'unique_department'
            )
        ]