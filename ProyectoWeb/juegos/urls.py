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
from . import views
from . import api_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.juegos, name="Juegos"),
    path('id=<int:id>/', views.game_detail, name='game_detail'),
    path('id=<int:id>/imprimir/', views.imprimir_juego, name='imprimir_juego'),

    # Vistas API
    path('api/v1/juegos/', api_views.juegos_list, name='juegos_list'),
    path('api/v1/juegos/<int:id>', api_views. game_detail_api, name=' game_detail_api'),
    
]

