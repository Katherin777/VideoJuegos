from django.shortcuts import render

# Create your views here.

# noticias/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia
from .forms import NoticiaForm

def noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'noticias/noticias.html', {'noticias': noticias})

def detalle_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticias/detalle_noticia.html', {'noticia': noticia})

def agregar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticias/agregar_noticia.html', {'form': form})

