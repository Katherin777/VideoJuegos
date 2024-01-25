from typing import Any
from django.db import models

# Create your models here.

class Juego(models.Model):

    nombre=models.CharField(max_length=50)
    plataforma=models.CharField(max_length=50)
    id_genero=models.CharField(max_length=50)
    creado=models.DateTimeField(auto_now_add=True)
    descripcion=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='juegos')

    class Meta:
        verbose_name='juego'
        verbose_name_plural='juegos'
    
    def __str__(self):
        return self.nombre