from django.shortcuts import render
from .models import Deelnemer
from koersen.models import KoersEditie, Deelnemer

#voor de lijst pagina
def deelnemer(request):
    deelnemers = Deelnemer.objects.all()
    return render(request, 'deelnemers/lijst.html', {'deelnemers':deelnemers})

from django.shortcuts import get_object_or_404
from collections import defaultdict

#voor de detail pagina
def deelnemer_detail(request, deelnemer_id):
    deelnemer = get_object_or_404(Deelnemer, id=deelnemer_id)
    zeges = KoersEditie.objects.filter(eerste_plaats=deelnemer).order_by('-jaar')
    zeges_per_jaar = defaultdict(list)
    for zege in zeges:
        zeges_per_jaar[zege.jaar].append(zege)

    #sorteren
    zeges_per_jaar = dict(sorted(zeges_per_jaar.items(), reverse=True))
    
       
    return render(request, 'deelnemers/detail.html', {'deelnemer': deelnemer, 'zeges_per_jaar': zeges_per_jaar})
