from django.db import models
from app.models import Location

class BedRoom(models.Model) :
    bedRoomType = (
            ('HOMME','Male'),('Femme', 'female')
        )
    
    numero = models.CharField(max_length=20, unique=True)
    categorie = models.CharField(choices=bedRoomType, max_length=10)
    status =  models.BooleanField(default=False)
    localisation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.numero
    
    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['numero', 'categorie', 'status', 'localisation'],
                name = 'unique_bedroom'
            )
        ]