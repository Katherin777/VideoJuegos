from django.shortcuts import render
from django.http.request import HttpRequest
from juegos.models import Juego
from django.db.models import Q


def juegos(request: HttpRequest):
    # Obtener los parámetros de filtro desde la solicitud
    nombre = request.GET.get('nombre')
    genero = request.GET.get('genero')
    plataforma = request.GET.get('plataforma')

    # Construir una consulta Q inicial vacía
    query = Q()

    # Añadir condiciones a la consulta Q según los parámetros recibidos
    if nombre:
        query &= Q(nombre__icontains=nombre)
    if genero:
        query &= Q(genero__icontains=genero)
    if plataforma:
        query &= Q(plataforma__icontains=plataforma)

    # Filtrar los juegos usando la consulta Q
    juegos = Juego.objects.filter(query)

    return render(request, "juegos/juegos.html", {"juegos": juegos})
