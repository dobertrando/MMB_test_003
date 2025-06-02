from django.db import models

# Create your models here.
class Deelnemer(models.Model):
    voornaam = models.CharField(max_length=64)
    achternaam = models.CharField(max_length=64)
    naamvoornaam = models.CharField(max_length=128, default='Voornaam Achternaam')
    status = models.CharField(max_length=64, default='Actief')
    ploegnaam = models.CharField(max_length=64, default='Geen ploegnaam')
    clan = models.CharField(max_length=64, default='Geen clan')

    def __str__(self):
        return f"{self.voornaam} {self.achternaam}"
    
    