from django.shortcuts import render
from juegos.models import Juego

# Create your views here.
def juegos(request):
    juegos=Juego.objects.all()
    return render(request, "juegos/juegos.html", {"juegos":juegos})
