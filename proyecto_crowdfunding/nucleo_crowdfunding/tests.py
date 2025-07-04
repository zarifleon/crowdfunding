from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import make_password
import json

from .models import CrowdUsuario, CrowdUsuarioNivel, CrowdCatalogoUsuarioTipo, CrowdCaso, CrowdCategoria, CrowdCatalogoEstatus

# --- Pruebas de Modelos ---
class CrowdUsuarioModelTest(TestCase):
    def test_str_representation(self):
        usuario = CrowdUsuario(
            id_morelia="TESTID001",
            email="test@example.com",
            password="testpassword", # No se hashea para prueba de __str__ simple
            first_name="NombrePrueba",
            last_name="ApellidoPrueba"
        )
        self.assertEqual(str(usuario), "NombrePrueba ApellidoPrueba (TESTID001)")

class CrowdCasoModelTest(TestCase):
    def setUp(self):
        self.creador = CrowdUsuario.objects.create(
            id_morelia="CREADOR01", email="creador@example.com", password="pwd",
            first_name="Creador", last_name="DeCasos"
        )
        self.categoria = CrowdCategoria.objects.create(nombre="Tecnología", descripcion="Proyectos tecnológicos")

    def test_str_representation(self):
        caso = CrowdCaso(
            creador=self.creador,
            exposicion_titulo="Mi Gran Proyecto Tech",
            exposicion_quien_soy="Soy un dev.",
            exposicion_que_necesito="Un nuevo servidor.",
            exposicion_porque="Para innovar.",
            exposicion_promocional="Apoya la innovación.",
            categoria=self.categoria,
            cantidad_requerida=50000.00,
            fecha_publicacion="2024-01-01", # Django convierte strings a date objects
            fecha_fin="2024-03-01"
        )
        self.assertEqual(str(caso), "Mi Gran Proyecto Tech")


# --- Pruebas de Vistas (API Endpoints) ---
# Usaremos RequestFactory para probar vistas sin pasar por todo el middleware de HTTP, o el cliente de Test de Django.

class RegistrarUsuarioVistaTest(TestCase):
    def setUp(self):
        self.url_registro = reverse('nucleo_crowdfunding:registrar_usuario')
        # Crear datos para tipos y niveles opcionales si se quieren probar
        self.tipo_usuario_basico, _ = CrowdCatalogoUsuarioTipo.objects.get_or_create(nombre="Básico")
        self.nivel_usuario_bronce, _ = CrowdUsuarioNivel.objects.get_or_create(nombre="Bronce", color="brown", icono_path="/icon.png")


    def test_registrar_nuevo_usuario_exitoso(self):
        data = {
            "id_morelia": "NUEVOID001",
            "email": "nuevo@example.com",
            "password": "password123",
            "first_name": "Nuevo",
            "last_name": "Usuario",
            "usuario_tipo_id": self.tipo_usuario_basico.id,
            "nivel_id": self.nivel_usuario_bronce.id
        }
        response = self.client.post(
            self.url_registro,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(CrowdUsuario.objects.filter(id_morelia="NUEVOID001").exists())

        # Verificar que la contraseña se hasheó (no es 'password123')
        usuario_creado = CrowdUsuario.objects.get(id_morelia="NUEVOID001")
        self.assertNotEqual(usuario_creado.password, "password123")
        self.assertTrue(len(usuario_creado.password) > 20) # Los hashes son largos

    def test_registrar_usuario_id_morelia_duplicado(self):
        CrowdUsuario.objects.create(
            id_morelia="EXISTENTE01", email="existente@example.com", password="pwd",
            first_name="Ya", last_name="Existe"
        )
        data = {
            "id_morelia": "EXISTENTE01", # ID Duplicado
            "email": "otroemail@example.com",
            "password": "password123",
            "first_name": "Otro",
            "last_name": "Usuario"
        }
        response = self.client.post(
            self.url_registro,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'El ID Morelia ya está registrado.')

    def test_registrar_usuario_email_duplicado(self):
        CrowdUsuario.objects.create(
            id_morelia="OTROID002", email="existente@example.com", password="pwd", # Email Duplicado
            first_name="Ya", last_name="ExisteMail"
        )
        data = {
            "id_morelia": "NUEVOID003",
            "email": "existente@example.com", # Email Duplicado
            "password": "password123",
            "first_name": "Otro",
            "last_name": "UsuarioMail"
        }
        response = self.client.post(
            self.url_registro,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'El correo electrónico ya está registrado.')

    def test_registrar_usuario_campos_faltantes(self):
        data = { # Falta 'email' y 'password'
            "id_morelia": "INCOMPLETO01",
            "first_name": "Incompleto",
            "last_name": "Datos"
        }
        response = self.client.post(
            self.url_registro,
            data=json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Faltan campos requeridos.')

# Se podrían añadir más pruebas para LoginUsuarioVistaTest, CrearCasoVistaTest, etc.
# Por ejemplo, para CrearCasoVistaTest:
# - Test de creación exitosa.
# - Test con creador_id_morelia inválido.
# - Test con categoria_id inválida.
# - Test con campos requeridos faltantes.
# - Test para verificar que los archivos se manejan (esto es más complejo y podría requerir mockear el storage).

# --- Pruebas Conceptuales para Frontend (Vue) ---
# Estas no se pueden ejecutar aquí, son solo para ilustrar.

# Ejemplo: test para TarjetaCaso.vue (usando sintaxis tipo Jest y Vue Test Utils)
#
# import { mount } from '@vue/test-utils'
# import TarjetaCaso from '@/componentes/TarjetaCaso.vue' // Ajustar path
#
# describe('TarjetaCaso.vue', () => {
#   it('calcula correctamente el porcentaje obtenido', () => {
#     const wrapper = mount(TarjetaCaso, {
#       props: {
#         caso: {
#           cantidad_obtenida: 50,
#           cantidad_requerida: 100
#         }
#       }
#     })
#     expect(wrapper.vm.porcentajeObtenido).toBe(50)
#   })
#
#   it('formatea la moneda correctamente', () => {
#     const wrapper = mount(TarjetaCaso, { /* ... */ });
#     expect(wrapper.vm.formatearMoneda(12345.67)).toBe('$12,345.67') // Ajustar según la salida exacta del método
#   })
#
#   it('trunca el texto correctamente', () => {
#      const wrapper = mount(TarjetaCaso, { /* ... */ });
#      const textoLargo = "Este es un texto muy largo que definitivamente necesita ser truncado para no ocupar demasiado espacio."
#      expect(wrapper.vm.truncarTexto(textoLargo, 20)).toBe('Este es un texto mu...')
#   })
#
#   it('renderiza el título del caso', () => {
#     const titulo = 'Mi Caso de Prueba'
#     const wrapper = mount(TarjetaCaso, {
#       props: { caso: { titulo: titulo, cantidad_obtenida: 0, cantidad_requerida: 100 } }
#     })
#     expect(wrapper.find('h3').text()).toBe(titulo)
#   })
# })
