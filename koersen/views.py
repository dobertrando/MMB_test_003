from django.shortcuts import render
from .models import Koers, KoersEditie, Deelnemer

#voor de lijst pagina
def koers(request):
    koersen = Koers.objects.all()
    return render(request, 'koersen/lijst.html', {'koersen':koersen})

#voor de detail pagina
from django.shortcuts import get_object_or_404
from collections import Counter
from itertools import chain

def koers_detail(request, koers_id):
    koers = get_object_or_404(Koers, id=koers_id)
    edities = KoersEditie.objects.filter(koers=koers).order_by('-jaar')

    #berekenen van de recordhouder
    winnaars_qs = Deelnemer.objects.filter(eerste_plaats__in=KoersEditie.objects.filter(koers=koers))
    winnaars = list(winnaars_qs)
    telling_namen = Counter(winnaars)
    max_wins = max(telling_namen.values())
    recordhouder = [naam for naam, aantal in telling_namen.items() if aantal == max_wins]

    #berekenen van het podiumbeest
    edities = KoersEditie.objects.filter(koers=koers)
    eerste_plaatsen = Deelnemer.objects.filter(eerste_plaats__in=edities)
    tweede_plaatsen = Deelnemer.objects.filter(tweede_plaats__in=edities)
    derde_plaatsen = Deelnemer.objects.filter(derde_plaats__in=edities)
    podiumdeelnemers = list(chain(eerste_plaatsen, tweede_plaatsen, derde_plaatsen))
   
    # deelnemer uitsluiten
    deelnemer_in_onderzoek = Deelnemer.objects.get(id=359)
    podiumdeelnemers = [d for d in podiumdeelnemers if d != deelnemer_in_onderzoek]

    podium_telling = Counter(podiumdeelnemers)
    max_podium = max(podium_telling.values(), default=0)
    podiumbeesten = [naam for naam, aantal in podium_telling.items() if aantal == max_podium]

    


    return render(request, 'koersen/detail.html', {'koers': koers, 'edities': edities, 'recordhouder': recordhouder, 'max_wins': max_wins, 'podiumbeesten': podiumbeesten, 'max_podium': max_podium})






