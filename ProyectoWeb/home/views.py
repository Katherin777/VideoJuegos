from django.shortcuts import render
from juegos.models import Juego  # Importar el modelo Game de la aplicación juegos
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home(request):
    juegos10 = Juego.objects.all()[:10]  # Obtener los primeros 10 juegos
    juegosRecientes = Juego.objects.all().order_by('-creado')[:10]  # Obtener los primeros 10 juegos ordenados por fecha más reciente
    #return render(request, 'home/list_games.html', {'games': games})
    context = {
        'juegos10': juegos10,
        'juegosRecientes': juegosRecientes,
    }
    return render(request, "home/home.html",  context)
   # return render(request, "home/home.html",  {'juegos': juegos})

#def list_games(request):
   # juegosLista = Juego.objects.all().order_by('id')[:10]  # Obtener los primeros 10 juegos ordenados por fecha más reciente
   #  return render(request, 'home/home.html', {'juegosLista': juegosLista})
def game_detail(request, id):
    juego = get_object_or_404(Juego, pk=id)
    context = {
        'juego': juego
    }
    return render(request, 'home/game_detail.html', context)
