from django.db import models
from app.models import Location

class BedRoom(models.Model) :
    bedRoomType = (
            ('M','Male'),('F', 'female')
        )
    
    number = models.CharField(max_length=20,unique=True)
    category = models.CharField(choices=bedRoomType, max_length=10)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.designation