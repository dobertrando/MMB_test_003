from django.db import models
from deelnemers.models import Deelnemer

# Create your models here.
class Koers(models.Model):
    naam = models.CharField(max_length=64)
    niveau = models.CharField(max_length=64)
    afkorting = models.CharField(max_length=64)
    land = models.CharField(max_length=64)
    volgnummer = models.CharField(max_length=64)


class KoersEditie(models.Model):
    koers = models.ForeignKey(Koers, on_delete=models.CASCADE, related_name='edities') #Elke editie hoort bij één koers  Als de koers verwijderd wordt, verdwijnen de edities ook  
    jaar = models.IntegerField()
    status = models.CharField(max_length=64)
    eerste_plaats = models.ManyToManyField(Deelnemer, related_name='eerste_plaats') #Eén editie kan meerdere winnaars hebben en vice versa
    tweede_plaats = models.ManyToManyField(Deelnemer, related_name='tweede_plaats') #renner.gewonnen_edities.all()` geeft alle gewonnen edities 
    derde_plaats = models.ManyToManyField(Deelnemer, related_name='derde_plaats')
  

