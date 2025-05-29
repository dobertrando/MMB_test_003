from django.shortcuts import render
from .models import Koers

#voor de lijst pagina
def koers(request):
    koersen = Koers.objects.all()
    return render(request, 'koersen/lijst.html', {'koersen':koersen})

