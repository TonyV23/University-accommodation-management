from django.db import models

class Student(models.Model) :
    GenderType = (
            ('M','Male'),('F', 'female')
        )
       
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(choices=GenderType, max_length=10)
    birth_date = models.DateField('date de naissance')
    inscription_date = models.DateField('date de naissance')
    
    def __str__(self) -> str:
        return self.designation