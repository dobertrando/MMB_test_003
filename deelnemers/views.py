from django.shortcuts import render
from .models import Deelnemer

def deelnemer(request):
    deelnemers = Deelnemer.objects.all()
    return render(request, 'deelnemers/fiche.html', {'deelnemers':deelnemers})


    