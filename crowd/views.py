from rest_framework import viewsets
from .models import (
    Usuario, UsuarioNivel, CatalogoUsuarioTipo, Categoria, CatalogoEstatus,
    SistemaMunicipalPrograma, Caso, Reaccion, Seguidor, ProgramaMunicipalBeneficiario,
    CasoArticulo, Votacion, CatalogoBancos, Factura, SistemaMunicipalProgramaFondeo,
    ReglasOperacion, Compromiso, CompromisoAbono, CompromisoEvidencia, Pregunta,
    CatalogoWalletMovimiento, Wallet, WalletMovimiento, SoporteMultimedia, Configuracion, Chat
)
from .serializers import (
    UsuarioSerializer, UsuarioNivelSerializer, CatalogoUsuarioTipoSerializer, CategoriaSerializer, CatalogoEstatusSerializer,
    SistemaMunicipalProgramaSerializer, CasoSerializer, ReaccionSerializer, SeguidorSerializer, ProgramaMunicipalBeneficiarioSerializer,
    CasoArticuloSerializer, VotacionSerializer, CatalogoBancosSerializer, FacturaSerializer, SistemaMunicipalProgramaFondeoSerializer,
    ReglasOperacionSerializer, CompromisoSerializer, CompromisoAbonoSerializer, CompromisoEvidenciaSerializer, PreguntaSerializer,
    CatalogoWalletMovimientoSerializer, WalletSerializer, WalletMovimientoSerializer, SoporteMultimediaSerializer, ConfiguracionSerializer, ChatSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioNivelViewSet(viewsets.ModelViewSet):
    queryset = UsuarioNivel.objects.all()
    serializer_class = UsuarioNivelSerializer

class CatalogoUsuarioTipoViewSet(viewsets.ModelViewSet):
    queryset = CatalogoUsuarioTipo.objects.all()
    serializer_class = CatalogoUsuarioTipoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CatalogoEstatusViewSet(viewsets.ModelViewSet):
    queryset = CatalogoEstatus.objects.all()
    serializer_class = CatalogoEstatusSerializer

class SistemaMunicipalProgramaViewSet(viewsets.ModelViewSet):
    queryset = SistemaMunicipalPrograma.objects.all()
    serializer_class = SistemaMunicipalProgramaSerializer

class CasoViewSet(viewsets.ModelViewSet):
    queryset = Caso.objects.all()
    serializer_class = CasoSerializer

class ReaccionViewSet(viewsets.ModelViewSet):
    queryset = Reaccion.objects.all()
    serializer_class = ReaccionSerializer

class SeguidorViewSet(viewsets.ModelViewSet):
    queryset = Seguidor.objects.all()
    serializer_class = SeguidorSerializer

class ProgramaMunicipalBeneficiarioViewSet(viewsets.ModelViewSet):
    queryset = ProgramaMunicipalBeneficiario.objects.all()
    serializer_class = ProgramaMunicipalBeneficiarioSerializer

class CasoArticuloViewSet(viewsets.ModelViewSet):
    queryset = CasoArticulo.objects.all()
    serializer_class = CasoArticuloSerializer

class VotacionViewSet(viewsets.ModelViewSet):
    queryset = Votacion.objects.all()
    serializer_class = VotacionSerializer

class CatalogoBancosViewSet(viewsets.ModelViewSet):
    queryset = CatalogoBancos.objects.all()
    serializer_class = CatalogoBancosSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class SistemaMunicipalProgramaFondeoViewSet(viewsets.ModelViewSet):
    queryset = SistemaMunicipalProgramaFondeo.objects.all()
    serializer_class = SistemaMunicipalProgramaFondeoSerializer

class ReglasOperacionViewSet(viewsets.ModelViewSet):
    queryset = ReglasOperacion.objects.all()
    serializer_class = ReglasOperacionSerializer

class CompromisoViewSet(viewsets.ModelViewSet):
    queryset = Compromiso.objects.all()
    serializer_class = CompromisoSerializer

class CompromisoAbonoViewSet(viewsets.ModelViewSet):
    queryset = CompromisoAbono.objects.all()
    serializer_class = CompromisoAbonoSerializer

class CompromisoEvidenciaViewSet(viewsets.ModelViewSet):
    queryset = CompromisoEvidencia.objects.all()
    serializer_class = CompromisoEvidenciaSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class CatalogoWalletMovimientoViewSet(viewsets.ModelViewSet):
    queryset = CatalogoWalletMovimiento.objects.all()
    serializer_class = CatalogoWalletMovimientoSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletMovimientoViewSet(viewsets.ModelViewSet):
    queryset = WalletMovimiento.objects.all()
    serializer_class = WalletMovimientoSerializer

class SoporteMultimediaViewSet(viewsets.ModelViewSet):
    queryset = SoporteMultimedia.objects.all()
    serializer_class = SoporteMultimediaSerializer

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
