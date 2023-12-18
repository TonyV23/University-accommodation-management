from django.db import models
from app.models import Student, Accommodation, Faculty, Department, Campus, Location, BedRoom
from django.contrib.auth.models import User

class Application(models.Model) :
    
    STATUS_CHOICES = (
        (1, "Accepter"),
        (0, "Rejeter"),
        (2, "En attente"),
    )
    
    matricule = models.CharField(max_length=20)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    departement = models.ForeignKey(Department, on_delete=models.CASCADE, help_text="S'il n'y a", null=True)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    entry_date = models.DateField(help_text="Vous devez mentionner la date précise e exacte mentionnée dans le Registre du Régent Responsable de votre regroupement. Si vous ne connaissez pas cette date, prière de la demander à votre Régent.")
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    bedroom = models.ForeignKey(BedRoom, on_delete=models.CASCADE)
    maquisard = models.BooleanField(help_text="Avez-vous un maquisard", default=True)
    residence_card_number = models.CharField(max_length=20)
    matricule_maquisard = models.CharField(max_length=20, help_text="Si vous n'avez pas de maquisard, ce numéro n'est pas obligatoire. Il est obligatoire si vous en avez.", null=True)
    residence_card_maquisard = models.CharField(max_length=20, help_text="N° de la carte de résidence du Maquisard", null=True)
    status = models.IntegerField(max_length=20, choices=STATUS_CHOICES, default=2)
    date_application = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.student.last_name+ " - "+self.student.first_name

    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['matricule','student','accommodation','maquisard','residence_card_number', 'date_application'],
                name = 'unique_bedroom_application'
            )
        ]