from django.db import models

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