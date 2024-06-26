from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import JuegoSerializer
from rest_framework.response import Response
from juegos.models import Juego, ClickCount
from django.db.models import Q
import json
from django.http import HttpResponse


@api_view(['GET'])
def juegos_list(request):
    nombre = request.GET.get('nombre')
    id_genero = request.GET.get('id_genero')
    plataforma = request.GET.get('plataforma')

    query = Q()
    if nombre:
        query &= Q(nombre__icontains=nombre)
    if id_genero:
        query &= Q(id_genero__icontains=id_genero)
    if plataforma:
        query &= Q(plataforma__icontains=plataforma)

    juegos = Juego.objects.filter(query)
    serializer = JuegoSerializer(juegos, many=True)
    #return Response(serializer.data)
    # Formatear el JSON con indentación
    formatted_json = json.dumps(serializer.data, indent=4)

    return HttpResponse(formatted_json, content_type='application/json')

@api_view(['GET'])
def game_detail_api(request, id):
    try:
        juego = Juego.objects.get(pk=id)
    except Juego.DoesNotExist:
        return Response(status=request.HTTP_404_NOT_FOUND)

    serializer = JuegoSerializer(juego)
    formatted_json = json.dumps(serializer.data, indent=4)
    return HttpResponse(formatted_json, content_type='application/json')
    #return Response(serializer.data)