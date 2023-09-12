from django.db import models

# Create your models here.

class Cours(models.Model):
    code_cours = models.CharField(max_length=10)
    titre = models.CharField(max_length=100)
    credits = models.PositiveIntegerField()
    programme_etudes = models.ForeignKey('ProgrammeEtudes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.code_cours} - {self.titre}"
    
    
    
class Bibliotheque(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)
    disponibilite = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titre} - {self.auteur}"
