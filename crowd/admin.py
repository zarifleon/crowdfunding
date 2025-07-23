from django.contrib import admin
from .models import (
    Usuario, UsuarioNivel, CatalogoUsuarioTipo, Categoria, CatalogoEstatus,
    SistemaMunicipalPrograma, Caso, Reaccion, Seguidor, ProgramaMunicipalBeneficiario,
    CasoArticulo, Votacion, CatalogoBancos, Factura, SistemaMunicipalProgramaFondeo,
    ReglasOperacion, Compromiso, CompromisoAbono, CompromisoEvidencia, Pregunta,
    CatalogoWalletMovimiento, Wallet, WalletMovimiento, SoporteMultimedia, Configuracion, Chat
)

admin.site.register(Usuario)
admin.site.register(UsuarioNivel)
admin.site.register(CatalogoUsuarioTipo)
admin.site.register(Categoria)
admin.site.register(CatalogoEstatus)
admin.site.register(SistemaMunicipalPrograma)
admin.site.register(Caso)
admin.site.register(Reaccion)
admin.site.register(Seguidor)
admin.site.register(ProgramaMunicipalBeneficiario)
admin.site.register(CasoArticulo)
admin.site.register(Votacion)
admin.site.register(CatalogoBancos)
admin.site.register(Factura)
admin.site.register(SistemaMunicipalProgramaFondeo)
admin.site.register(ReglasOperacion)
admin.site.register(Compromiso)
admin.site.register(CompromisoAbono)
admin.site.register(CompromisoEvidencia)
admin.site.register(Pregunta)
admin.site.register(CatalogoWalletMovimiento)
admin.site.register(Wallet)
admin.site.register(WalletMovimiento)
admin.site.register(SoporteMultimedia)
admin.site.register(Configuracion)
admin.site.register(Chat)
