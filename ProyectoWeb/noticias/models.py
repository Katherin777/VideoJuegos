#from django.db import models

# Create your models here.

# noticias/models.py
from django.db import models
from juegos.models import Juego

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='noticias')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

