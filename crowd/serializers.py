from rest_framework import serializers
from .models import (
    Usuario, UsuarioNivel, CatalogoUsuarioTipo, Categoria, CatalogoEstatus,
    SistemaMunicipalPrograma, Caso, Reaccion, Seguidor, ProgramaMunicipalBeneficiario,
    CasoArticulo, Votacion, CatalogoBancos, Factura, SistemaMunicipalProgramaFondeo,
    ReglasOperacion, Compromiso, CompromisoAbono, CompromisoEvidencia, Pregunta,
    CatalogoWalletMovimiento, Wallet, WalletMovimiento, SoporteMultimedia, Configuracion, Chat
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioNivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioNivel
        fields = '__all__'

class CatalogoUsuarioTipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoUsuarioTipo
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CatalogoEstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoEstatus
        fields = '__all__'

class SistemaMunicipalProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistemaMunicipalPrograma
        fields = '__all__'

class CasoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caso
        fields = '__all__'

class ReaccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaccion
        fields = '__all__'

class SeguidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguidor
        fields = '__all__'

class ProgramaMunicipalBeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaMunicipalBeneficiario
        fields = '__all__'

class CasoArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CasoArticulo
        fields = '__all__'

class VotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votacion
        fields = '__all__'

class CatalogoBancosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoBancos
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class SistemaMunicipalProgramaFondeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SistemaMunicipalProgramaFondeo
        fields = '__all__'

class ReglasOperacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReglasOperacion
        fields = '__all__'

class CompromisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compromiso
        fields = '__all__'

class CompromisoAbonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompromisoAbono
        fields = '__all__'

class CompromisoEvidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompromisoEvidencia
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'

class CatalogoWalletMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoWalletMovimiento
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class WalletMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletMovimiento
        fields = '__all__'

class SoporteMultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoporteMultimedia
        fields = '__all__'

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
