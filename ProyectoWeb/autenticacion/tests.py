from django.test import TestCase, RequestFactory
from django.urls import reverse
from autenticacion.views import VRegistro
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestAutenticacionViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_vregistro_get(self):
        url = reverse('Autenticacion')  # Nombre de la ruta para VRegistro
        request = self.factory.get(url)
        response = VRegistro.as_view()(request)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<form')  # Verifica que la etiqueta <form> esté en el contenido de la respuesta

    # Otras pruebas aquí...
    def test_creacion_usuario(self):
        # Crear un usuario de ejemplo
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Imprimir información del usuario creado (solo para fines de demostración)
        print(f"Usuario creado - Username: {user.username}, Password: testpassword")

        # Verificar que el usuario se haya creado correctamente
        self.assertEqual(User.objects.count(), 1)  # Verifica que solo haya un usuario en la base de datos
        self.assertEqual(user.username, 'testuser')  # Verifica el nombre de usuario

    def test_cerrar_sesion(self):
        # Simulamos un usuario autenticado
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_login(user)

        url = reverse('cerrar_sesion')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)  # Verifica que redireccione después de cerrar sesión
        self.assertFalse('_auth_user_id' in self.client.session)  # Verifica que el usuario no esté autenticado

    def test_logear_post_valid_credentials(self):
        User.objects.create_user(username='testuser', password='testpassword')

        url = reverse('logear')
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)  # Verifica redirección después de inicio de sesión válido
