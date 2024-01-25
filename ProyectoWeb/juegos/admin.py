from django.contrib import admin
from .models import Juego

# Register your models here.
class JuegoAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'creado')
    
    

admin.site.register(Juego, JuegoAdmin)