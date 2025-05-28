from django.shortcuts import render
from .models import Deelnemer

#voor de lijst pagina
def deelnemer(request):
    deelnemers = Deelnemer.objects.all()
    return render(request, 'deelnemers/lijst.html', {'deelnemers':deelnemers})

from django.shortcuts import get_object_or_404

#voor de detail pagina
def deelnemer_detail(request, deelnemer_id):
    deelnemer = get_object_or_404(Deelnemer, id=deelnemer_id)
    return render(request, 'deelnemers/detail.html', {'deelnemer': deelnemer})
