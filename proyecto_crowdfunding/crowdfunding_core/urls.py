from django.urls import path
from . import views

app_name = 'crowdfunding_core' # Renamed app_name

urlpatterns = [
    # Autenticación
    path('usuarios/registrar/', views.registrar_usuario_vista, name='registrar_usuario'),
    path('usuarios/login/', views.login_usuario_vista, name='login_usuario'),

    # Gestión de Casos (CRUD)
    path('casos/', views.listar_casos_vista, name='listar_casos'),
    path('casos/crear/', views.crear_caso_vista, name='crear_caso'),
    path('casos/<int:caso_id>/', views.detalle_caso_vista, name='detalle_caso'),
    path('casos/<int:caso_id>/actualizar/', views.actualizar_caso_vista, name='actualizar_caso'),
    path('casos/<int:caso_id>/eliminar/', views.eliminar_caso_vista, name='eliminar_caso'),
]
