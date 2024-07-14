from django.urls import path
from . import views, api_views

urlpatterns = [
    path('juegos/<int:id>/comment/', views.add_comment_to_game, name='add_comment_to_game'),
    path('comment/edit/<int:id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:id>/', views.delete_comment, name='delete_comment'),

    path('api/v1/<int:id>/', api_views.comentario_detalle_api, name='comentario_detalle_api'),
    path('api/v1/ ', api_views.comentario_crear_api, name='comentario_crear_api'),
    path('api/v1/  ', api_views.comentario_actualizar_api, name='comentario_actualizar_api'),
    
]
