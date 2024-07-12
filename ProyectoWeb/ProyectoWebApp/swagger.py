from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API de Videojuegos",
        default_version='v1',
        description="Documentación de la API de la base de datos de videojuegos",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contacto@ejemplo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
