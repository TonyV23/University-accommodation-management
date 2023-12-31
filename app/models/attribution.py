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
    student = models.OneToOneField(Application, on_delete=models.CASCADE)
    bedroom = models.OneToOneField(BedRoom, on_delete=models.CASCADE)
    payment_method = models.CharField(choices=payment_mode, max_length=20)
    amount_paid = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency='BIF')
    date_attribution = models.DateField(auto_now_add=True)

    def delete_application(self):
        self.student.delete()
        self.delete()

    def save(self, **kwargs):
        if self.pk is not None:
            self.delete_application()
        super(Attribution, self).save(**kwargs)

post_save.connect(update_bedroom_status, sender=Attribution)
