from django.shortcuts import render
from juegos.models import Juego  # Importar el modelo Game de la aplicación juegos
from django.shortcuts import render, get_object_or_404
from juegos.models import ClickCount  # Importa el modelo ClickCount de la otra aplicación
from django.db.models import Sum

# Create your views here.
def home(request):
   # Obtener los juegos más visualizados ordenados por el conteo de clics
    juegosMasVisualizados = Juego.objects.annotate(num_clicks=Sum('click_count__count')).order_by('-num_clicks')[:10]
    juegos10 = Juego.objects.all()[:10]  # Obtener los primeros 10 juegos
    juegosRecientes = Juego.objects.all().order_by('-creado')[:10]  # Obtener los primeros 10 juegos ordenados por fecha más reciente
    #return render(request, 'home/list_games.html', {'games': games})
    context = {
        'juegosMasVisualizados': juegosMasVisualizados,
        'juegos10': juegos10,
        'juegosRecientes': juegosRecientes,
    }
    return render(request, "home/home.html",  context)
   # return render(request, "home/home.html",  {'juegos': juegos})

#def list_games(request):
   # juegosLista = Juego.objects.all().order_by('id')[:10]  # Obtener los primeros 10 juegos ordenados por fecha más reciente
   #  return render(request, 'home/home.html', {'juegosLista': juegosLista})
#def game_detail(request, id):
 #   juego = get_object_or_404(Juego, pk=id)
  #  context = {
   #     'juego': juego
   # }
    #return render(request, 'home/game_detail.html', context)
