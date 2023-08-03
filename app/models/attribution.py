from django.db import models
from django.db.models.signals import post_save

from app.models import Student, BedRoom

def update_bedroom_status(sender, instance, created, **kwargs):
    bedroom = instance.bedroom
    bedroom.status = True
    bedroom.save()

class Attribution(models.Model) :
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bedroom = models.ForeignKey(BedRoom, on_delete=models.CASCADE)
    date_attribution = models.DateField(auto_now_add=True)

    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['student', 'bedroom', 'date_attribution'],
                name = 'unique_attribution'
            )
        ]
    
post_save.connect(update_bedroom_status, sender= Attribution)  