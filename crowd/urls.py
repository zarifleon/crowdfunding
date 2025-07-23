from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet, UsuarioNivelViewSet, CatalogoUsuarioTipoViewSet, CategoriaViewSet, CatalogoEstatusViewSet,
    SistemaMunicipalProgramaViewSet, CasoViewSet, ReaccionViewSet, SeguidorViewSet, ProgramaMunicipalBeneficiarioViewSet,
    CasoArticuloViewSet, VotacionViewSet, CatalogoBancosViewSet, FacturaViewSet, SistemaMunicipalProgramaFondeoViewSet,
    ReglasOperacionViewSet, CompromisoViewSet, CompromisoAbonoViewSet, CompromisoEvidenciaViewSet, PreguntaViewSet,
    CatalogoWalletMovimientoViewSet, WalletViewSet, WalletMovimientoViewSet, SoporteMultimediaViewSet, ConfiguracionViewSet, ChatViewSet
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'usuario-niveles', UsuarioNivelViewSet)
router.register(r'catalogo-usuario-tipos', CatalogoUsuarioTipoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'catalogo-estatus', CatalogoEstatusViewSet)
router.register(r'sistema-municipal-programas', SistemaMunicipalProgramaViewSet)
router.register(r'casos', CasoViewSet)
router.register(r'reacciones', ReaccionViewSet)
router.register(r'seguidores', SeguidorViewSet)
router.register(r'programa-municipal-beneficiarios', ProgramaMunicipalBeneficiarioViewSet)
router.register(r'caso-articulos', CasoArticuloViewSet)
router.register(r'votaciones', VotacionViewSet)
router.register(r'catalogo-bancos', CatalogoBancosViewSet)
router.register(r'facturas', FacturaViewSet)
router.register(r'sistema-municipal-programa-fondeos', SistemaMunicipalProgramaFondeoViewSet)
router.register(r'reglas-operaciones', ReglasOperacionViewSet)
router.register(r'compromisos', CompromisoViewSet)
router.register(r'compromiso-abonos', CompromisoAbonoViewSet)
router.register(r'compromiso-evidencias', CompromisoEvidenciaViewSet)
router.register(r'preguntas', PreguntaViewSet)
router.register(r'catalogo-wallet-movimientos', CatalogoWalletMovimientoViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'wallet-movimientos', WalletMovimientoViewSet)
router.register(r'soporte-multimedias', SoporteMultimediaViewSet)
router.register(r'configuraciones', ConfiguracionViewSet)
router.register(r'chats', ChatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
