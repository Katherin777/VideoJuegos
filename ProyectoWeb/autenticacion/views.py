from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserCreationFormWithEmail
from django.contrib.messages import error, success


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


class VRegistro(View):

    def get(self, request):
        form = UserCreationFormWithEmail()
        return render(request, "autenticacion/autenticacion.html", {"form":form})
    
    def post(self, request):
        #form=UserCreationForm(request.POST)
        form = UserCreationFormWithEmail(request.POST)

        if form.is_valid():

            #usuario=form.save()

            #login(request, usuario)

            #return redirect('Home')
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)
            success(request, "¡Registro exitoso!")
            return redirect('Home')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,"autenticacion/autenticacion.html",{"form":form})

        

def cerrar_sesion(request):
        logout(request)
        return redirect('Home')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                for msg in form.error_messages:
                    messages.error(request, form.error_messages[msg])
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})

@login_required
def eliminar_usuario(request):
    if request.method == "POST":
        usuario = request.user
        usuario.delete()
        messages.success(request, "Tu cuenta ha sido eliminada exitosamente.")
        return redirect('Home')
    return render(request, "eliminar_usuario/eliminar_usuario.html")