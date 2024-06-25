from django.contrib import admin
from .models import Juego, ClickCount

# Register your models here.
class JuegoAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'creado')
    
    

admin.site.register(Juego, JuegoAdmin)


class ClickCountAdmin(admin.ModelAdmin):
    list_display = ('juego_id', 'juego_nombre', 'count')

    def juego_id(self, obj):
        return obj.juego.id
    juego_id.short_description = 'Juego ID'

    def juego_nombre(self, obj):
        return obj.juego.nombre
    juego_nombre.short_description = 'Nombre del Juego'

#admin.site.register(Juego)
admin.site.register(ClickCount, ClickCountAdmin)
