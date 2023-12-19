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
    etudiant = models.OneToOneField(Student, on_delete=models.CASCADE)
    faculte = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    departement = models.ForeignKey(Department, on_delete=models.CASCADE, help_text="S'il n'y a", null=True)
    logement = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    date_entree = models.DateField(help_text="Vous devez mentionner la date précise e exacte mentionnée dans le Registre du Régent Responsable de votre regroupement. Si vous ne connaissez pas cette date, prière de la demander à votre Régent.")
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    localisation = models.ForeignKey(Location, on_delete=models.CASCADE)
    chambre = models.ForeignKey(BedRoom, on_delete=models.CASCADE)
    maquisard = models.BooleanField(help_text="Avez-vous un maquisard", default=True)
    numero_carte_de_residence = models.CharField(max_length=20)
    matricule_maquisard = models.CharField(max_length=20, help_text="Si vous n'avez pas de maquisard, ce numéro n'est pas obligatoire. Il est obligatoire si vous en avez.", null=True)
    maquisard_carte_de_residence = models.CharField(max_length=20, help_text="N° de la carte de résidence du Maquisard", null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    date_de_demande = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.etudiant.nom+ " - "+self.etudiant.prenom

    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['matricule','etudiant','status'],
                name = 'unique_chambre_application'
            )
        ]