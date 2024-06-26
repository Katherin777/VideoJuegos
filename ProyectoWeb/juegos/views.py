from django.shortcuts import render, get_object_or_404
from django.http.request import HttpRequest
from juegos.models import Juego, ClickCount
from django.db.models import Q


def juegos(request: HttpRequest):
    # Obtener los parámetros de filtro desde la solicitud
    nombre = request.GET.get('nombre')
    id_genero = request.GET.get('id_genero')
    plataforma = request.GET.get('plataforma')

    # Construir una consulta Q inicial vacía
    query = Q()

    # Añadir condiciones a la consulta Q según los parámetros recibidos
    if nombre:
        query &= Q(nombre__icontains=nombre)
    if id_genero:
        query &= Q(genero__icontains=id_genero)
    if plataforma:
        query &= Q(plataforma__icontains=plataforma)

    # Filtrar los juegos usando la consulta Q
    juegos = Juego.objects.filter(query)

    return render(request, "juegos/juegos.html", {"juegos": juegos})

def game_detail(request, id):
    juego = get_object_or_404(Juego, pk=id)

        # Incrementar el contador de clics
    click_count, created = ClickCount.objects.get_or_create(juego=juego)
    click_count.count += 1
    click_count.save()
    context = {
        'juego': juego
    }
    return render(request, 'juegos/game_detail.html', context)



