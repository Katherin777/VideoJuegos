from django.shortcuts import render, HttpResponse

# Create your views here.

#def home(request):

    #return render(request, "ProyectoWebApp/home.html")


#def noticias(request):
    
    #return render(request, "ProyectoWebApp/noticias.html")
from juegos.models import Juego
from noticias.models import Noticia  # Asegúrate de importar tus modelos

def buscar(request):
    query = request.GET.get('q')
    juegos_resultados = []
    noticias_resultados = []

    if query:
        juegos_resultados = Juego.objects.filter(nombre__icontains=query)
        noticias_resultados = Noticia.objects.filter(titulo__icontains=query)

    context = {
        'query': query,
        'juegos_resultados': juegos_resultados,
        'noticias_resultados': noticias_resultados,
    }
    return render(request, 'ProyectoWebApp/resultados_busqueda.html', context)

def detalle_juego(request, id):
    juego = Juego.objects.get(id=id)
    return render(request, 'juegos/game_detail.html', {'juego': juego})

def detalle_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    return render(request, 'detalle_noticia.html', {'noticia': noticia})

