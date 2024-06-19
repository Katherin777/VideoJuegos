from django import forms
from .models import Comentarios

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['contenido']
