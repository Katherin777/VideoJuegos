from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage


def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid:
                nombre=request.POST.get("nombre")
                email=request.POST.get("email")
                contenido=request.POST.get("contenido")

                email=EmailMessage("Mensaje desde App Django",
                contenido,email,["katherin_carina06@hotmail.com"])

                try:
                    email.send()

                    return redirect("/contacto/?valido")
                except:
                    return redirect("/contacto/?novalido")
                     
                
    
    return render(request, "contacto/contacto.html", {"miFormulario":formulario_contacto})