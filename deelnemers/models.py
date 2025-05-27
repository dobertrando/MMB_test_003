from django.db import models

# Create your models here.
class Deelnemer(models.Model):
    voornaam = models.CharField(max_length=64)
    achternaam = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    ploegnaam = models.CharField(max_length=64)
    clan = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    foto = models.ImageField(upload_to='deelnemers_fotos/', blank=True, null=True)
    