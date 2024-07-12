from django.urls import path
from . import views

urlpatterns = [
    path('juegos/<int:id>/comment/', views.add_comment_to_game, name='add_comment_to_game'),
    path('comment/edit/<int:id>/', views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:id>/', views.delete_comment, name='delete_comment'),
]
