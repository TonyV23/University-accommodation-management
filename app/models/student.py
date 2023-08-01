from django.db import models
from app.models import Faculty, Department

class Student(models.Model) :
    GenderType = (
            ('M','Male'),('F', 'female')
        )
       
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(choices=GenderType, max_length=10)
    birth_date = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    inscription_number = models.PositiveIntegerField()
    inscription_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.first_name+" - "+self.last_name
    
    class Meta :
         constraints = [
            models.UniqueConstraint(
                fields = ['first_name', 'last_name', 'gender', 'birth_date','faculty', 'department' ,'inscription_date', 'inscription_number'],
                name = 'unique_student'
            )
        ]