from django.urls import path
from . import views

urlpatterns = [
    path('juegos/<int:id>/comment/', views.add_comment_to_game, name='add_comment_to_game'),
]
