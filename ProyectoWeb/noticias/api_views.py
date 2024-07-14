from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from .serializers import NoticiaSerializer
from rest_framework.response import Response
from .models import Noticia
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get', 
    responses={
        200: NoticiaSerializer(),
        204: 'No Content',
        401: 'Unauthorized',
        403: 'Forbidden',
        405: 'Method Not Allowed',
        500: 'Error interno del servidor'
    }
)
@api_view(['GET'])
def noticia_detalle(request, id):
    noticia = get_object_or_404(Noticia, pk=id)
    serializer = NoticiaSerializer(noticia)
    return Response(serializer.data)

@swagger_auto_schema(
    method='get', 
    responses=
    {
        200: NoticiaSerializer(many=True),
        204: 'No Content',
        401: 'Unauthorized',
        403: 'Forbidden',
        405: 'Method Not Allowed',
        500: 'Error interno del servidor'}
)
@api_view(['GET'])
def listar_noticias(request):
    noticias = Noticia.objects.all()
    serializer = NoticiaSerializer(noticias, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=NoticiaSerializer, responses={201: NoticiaSerializer()})
@api_view(['POST'])
def crear_noticia(request):
    serializer = NoticiaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=NoticiaSerializer, responses={200: NoticiaSerializer()})
@api_view(['PUT'])
def actualizar_noticia(request, id):
    noticia = get_object_or_404(Noticia, pk=id)
    serializer = NoticiaSerializer(noticia, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'})
@api_view(['DELETE'])
def eliminar_noticia(request, id):
    noticia = get_object_or_404(Noticia, pk=id)
    noticia.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)