from django.shortcuts import render, HttpResponse
from juegos.models import Juego
from juegos.serializers import serializers
from noticias.models import Noticia  # Asegúrate de importar tus modelos
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
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
    return render(request, 'game_detail.html', {'juego': juego})

def detalle_noticia(request, id):
    noticia = Noticia.objects.get(id=id)
    return render(request, 'detalle_noticia.html', {'noticia': noticia})

@api_view(['GET'])
def juego_detalle_api(request, id):
    juego = get_object_or_404(Juego, pk=id)
    data = {
        'nombre': juego.nombre,
        'genero': juego.id_genero.nombre,  # Asumiendo que tienes una relación con un modelo Género
        'plataforma': juego.plataforma.nombre,  # Asumiendo que tienes una relación con un modelo Plataforma
        'imagen': juego.imagen.url,
    }
    return JsonResponse(data)

@api_view(['POST'])
def juego_crear_api(request):
    if request.method == 'POST':
        serializer = serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'nombre': serializer.data['nombre'],
                'genero': serializer.data['id_genero'],
                'plataforma': serializer.data['plataforma'],
                'imagen': serializer.data['imagen'],
            }
            return JsonResponse(data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


