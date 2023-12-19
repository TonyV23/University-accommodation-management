from django.db import models
import random
from app.models import Faculty, Department, Campus

class Student(models.Model) :
    GenderType = (
            ('M','Male'),('F', 'female')
        )
       
    prenom = models.CharField(max_length=20)
    nom = models.CharField(max_length=20)
    genre = models.CharField(choices=GenderType, max_length=10)
    date_de_naissance = models.DateField()
    faculte = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    departement = models.ForeignKey(Department, on_delete=models.CASCADE)
    numero_inscription = models.PositiveIntegerField()
    date_inscription = models.DateField(auto_now_add=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=4, unique=True)

    def save(self, *args, **kwargs):
        # Generate a 4-digit random matricule
        self.matricule = str(random.randint(1000, 9999))
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.prenom+" - "+self.nom
    
    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['prenom', 'nom', 'genre', 'date_de_naissance','faculte', 'departement' ,'date_inscription', 'numero_inscription'],
                name = 'unique_student'
            )
        ]