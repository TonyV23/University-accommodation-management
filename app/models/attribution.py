from django.db import models
from django.db.models.signals import post_save
from djmoney.models.fields import MoneyField

from app.models import Application, BedRoom


def update_bedroom_status(sender, instance, created, **kwargs):
    bedroom = instance.bedroom
    bedroom.status = True
    bedroom.save()

class Attribution(models.Model):
    payment_mode = (('via banque', 'via banque'), ('cash', 'cash'))
    student = models.ForeignKey(Application, on_delete=models.CASCADE)
    bedroom = models.ForeignKey(BedRoom, on_delete=models.CASCADE)
    payment_method = models.CharField(choices=payment_mode, max_length=20)
    amount_paid = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency='BIF')
    date_attribution = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'bedroom', 'date_attribution'],
                name='unique_attribution'
            )
        ]

post_save.connect(update_bedroom_status, sender=Attribution)
