from django.db import models
from app.models import Location

class BedRoom(models.Model) :
    bedRoomType = (
            ('HOMME','Male'),('Femme', 'female')
        )
    
    number = models.CharField(max_length=20, unique=True)
    category = models.CharField(choices=bedRoomType, max_length=10)
    status =  models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.number
    
    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['number', 'category', 'status', 'location'],
                name = 'unique_bedroom'
            )
        ]