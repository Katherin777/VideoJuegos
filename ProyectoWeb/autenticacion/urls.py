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
from django.conf import settings
from django.conf.urls.static import static
from .views import VRegistro, cerrar_sesion, logear, eliminar_usuario
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
    path('eliminar_usuario', eliminar_usuario, name="eliminar_usuario"),  # Nueva ruta para eliminar usuario
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="reset_password/reset_password.html"), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent/reset_password_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password_form/reset_password_form.html"), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_done/reset_password_done.html"), name="password_reset_complete"),
]

