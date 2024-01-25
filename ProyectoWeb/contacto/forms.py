from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required="true")
    email = forms.CharField(label="Email", required="true")
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)
    """your_name = forms.CharField(label="Your name", max_length=100)"""