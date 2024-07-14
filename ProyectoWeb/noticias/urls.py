"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views, api_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.noticias, name="Noticias"),
    path('id=<int:noticia_id>', views.detalle_noticia, name='detalle_noticia'),

        # Vistas API
    path('api/v1/', api_views.listar_noticias, name='listar_noticias'),
    path('api/v1/<int:id>/', api_views.noticia_detalle, name='noticia_detalle'),
    path('api/v1/ ', api_views.crear_noticia, name='crear_noticia'),
    path('api/v1/  ', api_views.actualizar_noticia, name='actualizar_noticia'),
    path('api/v1/<int:id>/eliminar/', api_views.eliminar_noticia, name='eliminar_noticia'),
]

