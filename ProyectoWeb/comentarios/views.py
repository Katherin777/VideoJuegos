#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comentarios
from juegos.models import Juego  # Importa el modelo Juego desde la aplicación juegos
from .forms import CommentForm

@login_required
def add_comment_to_game(request, id):
    juego = get_object_or_404(Juego, pk=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.juego = juego
            comentario.usuario = request.user
            comentario.save()
            return redirect('game_detail', id=juego.id)
    else:
        form = CommentForm()

    return render(request, 'comentarios/add_comment_to_game.html', {'form': form})

@login_required
def edit_comment(request, id):
    comentario = get_object_or_404(Comentarios, pk=id)

    if request.user != comentario.usuario:
        return redirect('game_detail', id=comentario.juego.id)  # Redirige si el usuario no es el autor

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('game_detail', id=comentario.juego.id)
    else:
        form = CommentForm(instance=comentario)

    return render(request, 'comentarios/edit_comment.html', {'form': form})

@login_required
def delete_comment(request, id):
    comentario = get_object_or_404(Comentarios, pk=id)

    if request.user != comentario.usuario:
        return redirect('game_detail', id=comentario.juego.id)  # Redirige si el usuario no es el autor

    if request.method == 'POST':
        comentario.delete()
        return redirect('game_detail', id=comentario.juego.id)

    return render(request, 'comentarios/delete_comment.html', {'comentario': comentario})

