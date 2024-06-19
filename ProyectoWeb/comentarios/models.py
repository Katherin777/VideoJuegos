from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from juegos.models import Juego  # Importa el modelo Juego desde la aplicación juegos

class Comentarios(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='comments')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username} en {self.juego.nombre}'
