from django.db import models
from deelnemers.models import Deelnemer

# Create your models here.
class Koers(models.Model):
    naam = models.CharField(max_length=64)
    niveau = models.CharField(max_length=64)
    afkorting = models.CharField(max_length=64)
    land = models.CharField(max_length=64)
    koersvolgnummer = models.CharField(max_length=64)
    class Meta:
        verbose_name = 'Koers'
        verbose_name_plural = 'Koersen' # voor de admin interface
    def __str__(self):
        return f"{self.naam}"

class KoersEditie(models.Model):
    jaar = models.IntegerField()
    koers = models.ForeignKey(Koers, on_delete=models.CASCADE)
    editie = models.CharField(max_length=64)
    koersstatus = models.CharField(max_length=64)
    eerste_plaats = models.ManyToManyField(Deelnemer, related_name='eerste_plaats')
    tweede_plaats = models.ManyToManyField(Deelnemer, related_name='tweede_plaats')
    derde_plaats = models.ManyToManyField(Deelnemer, related_name='derde_plaats')
    uitslagstatus = models.CharField(max_length=64)
    jaar = models.IntegerField()

    def __str__(self):
        return f"{self.koers} in {self.jaar}"
