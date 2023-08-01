from django.db import models

class Faculty(models.Model) :
    designation = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.designation