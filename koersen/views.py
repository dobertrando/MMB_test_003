from django.shortcuts import render
from .models import Koers, KoersEditie

#voor de lijst pagina
def koers(request):
    koersen = Koers.objects.all()
    return render(request, 'koersen/lijst.html', {'koersen':koersen})

from django.shortcuts import get_object_or_404

def koers_detail(request, koers_id):
    koers = get_object_or_404(Koers, id=koers_id)
    edities = KoersEditie.objects.filter(koers=koers).order_by('-jaar')
    return render(request, 'koersen/detail.html', {'koers': koers, 'edities': edities})

