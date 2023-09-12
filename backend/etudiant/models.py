from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Niveau(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=10, unique=True)
    annee_etudes = models.PositiveIntegerField()
    duree_typique = models.PositiveIntegerField()  # en années
    
    def __str__(self):
        return self.nom

class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    code = models.UUIDField(max_length=10)
    statut = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    
    
class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='etudiant')
    date_naissance = models.DateField()
    adresse = models.TextField()
    telephone = models.CharField(max_length=15)
    piece_identite = models.FileField(upload_to="/piece_ientites", blank=True, null=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"
    
    @property
    def age(self):
        today = date.today()
        born = self.date_naissance
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    