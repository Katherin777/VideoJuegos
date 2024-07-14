from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import ComentarioSerializer
from rest_framework.response import Response
from .models import Comentarios
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    operation_description="Obtener comentarios por ID",
    responses={
        200: ComentarioSerializer,
        204: 'No Content',
        401: 'Unauthorized',
        403: 'Forbidden',
        405: 'Method Not Allowed',
        500: 'Error interno del servidor'
    }
)


@api_view(['GET'])
def comentario_detalle_api(request, id):
    comentario = get_object_or_404(Comentarios, pk=id)
    serializer = ComentarioSerializer(comentario)
    return Response(serializer.data)

@swagger_auto_schema(
    method='post',
    operation_description="Insertar comentario",
    responses={
        200: ComentarioSerializer,
        401: 'Unauthorized',
        403: 'Forbidden',
        405: 'Method Not Allowed',
        500: 'Error interno del servidor'
    }
)
@api_view(['POST'])
def comentario_crear_api(request):
    if request.method == 'POST':
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(
    method='put',
    operation_description="Actualizar comentario",
    responses={
        200: ComentarioSerializer,
        401: 'Unauthorized',
        403: 'Forbidden',
        405: 'Method Not Allowed',
        500: 'Error interno del servidor'
    }
)

@api_view(['PUT'])
def comentario_actualizar_api(request, id):
    comentario = get_object_or_404(Comentarios, pk=id)
    if request.method == 'PUT':
        serializer = ComentarioSerializer(comentario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)