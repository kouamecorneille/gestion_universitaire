from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Matiere(models.Model):
    
    pass


class Enseignant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='professeur')
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    #matiere_enseignee = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"


