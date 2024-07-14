from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import JuegoSerializer
from rest_framework.response import Response
from juegos.models import Juego, ClickCount
from django.db.models import Q
import json
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    operation_description="Obtener lista de juegos",
    responses={
        200: JuegoSerializer(many=True),
        204: 'No Content',
        401: 'Unauthorized',
        403: 'Forbidden',
        405: 'Method Not Allowed',
        500: 'Error interno del servidor'
    }
)

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

@swagger_auto_schema(
    method='get',
    operation_description="Obtener juego por ID",
    responses={
        200: JuegoSerializer,
        204: 'No Content',
        401: 'Unauthorized',
        403: 'Forbidden',
        405: 'Method Not Allowed',
        500: 'Error interno del servidor'
    }
)

@api_view(['GET'])
def game_detail_api(request, id):
    try:
        juego = Juego.objects.get(pk=id)
    except Juego.DoesNotExist:
        return Response(status=request.HTTP_404_NOT_FOUND)

    serializer = JuegoSerializer(juego)
    formatted_json = json.dumps(serializer.data, indent=4)
    return HttpResponse(formatted_json, content_type='application/json')

@swagger_auto_schema(
    method='post',
    operation_description="Crear juego",
    responses={
        200: JuegoSerializer,
        401: 'Unauthorized',
        403: 'Forbidden',
        405: 'Method Not Allowed',
        500: 'Error interno del servidor'
    }
)

@api_view(['POST'])
def juego_crear_api(request):
    if request.method == 'POST':
        serializer = JuegoSerializer(data=request.data)
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
    
@swagger_auto_schema(
    method='put',
    operation_description="Actualizar juego",
    responses={
        200: JuegoSerializer,
        401: 'Unauthorized',
        403: 'Forbidden',
        405: 'Method Not Allowed',
        500: 'Error interno del servidor'
    }
)
    
@api_view(['PUT'])
def juego_actualizar_api(request, id):
    juego = get_object_or_404(Juego, pk=id)
    if request.method == 'PUT':
        serializer = JuegoSerializer(juego, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'nombre': serializer.data['nombre'],
                'genero': serializer.data['id_genero'],
                'plataforma': serializer.data['plataforma'],
                'imagen': serializer.data['imagen'],
            }
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
