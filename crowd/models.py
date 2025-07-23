from django.db import models

class UsuarioNivel(models.Model):
    nombre = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    icono_path = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class CatalogoUsuarioTipo(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id_morelia = models.CharField(max_length=255, unique=True, primary_key=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    usuario_tipo = models.ForeignKey(CatalogoUsuarioTipo, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    nivel = models.ForeignKey(UsuarioNivel, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class CatalogoEstatus(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class SistemaMunicipalPrograma(models.Model):
    descripcion_nombre = models.TextField(blank=True, null=True)
    descripcion_detalles = models.TextField(blank=True, null=True)
    presupuesto_total = models.FloatField(blank=True, null=True)
    presupuesto_disponible = models.FloatField(blank=True, null=True)
    presupuesto_meta = models.FloatField(blank=True, null=True)
    estatus = models.CharField(max_length=1)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    cuenta_bancaria = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.descripcion_nombre

class Caso(models.Model):
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='casos_creados')
    exposicion_titulo = models.CharField(max_length=255)
    exposicion_quien_soy = models.TextField()
    exposicion_que_necesito = models.TextField()
    exposicion_porque = models.TextField()
    exposicion_detalles_adicionales = models.TextField()
    exposicion_promocional = models.TextField()
    video_promocional = models.TextField(blank=True, null=True)
    imagen_promocional = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad_requerida = models.FloatField()
    cantidad_obtenida = models.FloatField()
    estatus = models.ForeignKey(CatalogoEstatus, on_delete=models.SET_NULL, null=True)
    fecha_publicacion = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateField()
    municipal_programa = models.ForeignKey(SistemaMunicipalPrograma, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.exposicion_titulo

class Reaccion(models.Model):
    TIPO_INTERACCION_CHOICES = [
        ('L', 'Like'),
        ('M', 'Me encanta'),
    ]
    tipo_interaccion = models.CharField(max_length=1, choices=TIPO_INTERACCION_CHOICES)
    promotor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

class Seguidor(models.Model):
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='seguidores')
    promotor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='siguiendo')
    fecha = models.DateTimeField(auto_now_add=True)

class ProgramaMunicipalBeneficiario(models.Model):
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    caso = models.ForeignKey(Caso, on_delete=models.SET_NULL, null=True, blank=True)
    municipal_programa = models.ForeignKey(SistemaMunicipalPrograma, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=1)

class CasoArticulo(models.Model):
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    recibo_tipo = models.CharField(max_length=255)
    precio = models.FloatField()

class Votacion(models.Model):
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    municipal_programa = models.ForeignKey(SistemaMunicipalPrograma, on_delete=models.CASCADE)
    promotor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

class CatalogoBancos(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    datos = models.TextField(blank=True, null=True)
    id_empresa = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='facturas_emitidas')
    id_ciudadano = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='facturas_recibidas')

class SistemaMunicipalProgramaFondeo(models.Model):
    promotor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    monto = models.FloatField()
    cuenta_bancaria = models.CharField(max_length=255)
    banco = models.ForeignKey(CatalogoBancos, on_delete=models.CASCADE)
    transaccion = models.CharField(max_length=255)
    codigo_verificacion = models.CharField(max_length=255)
    estatus = models.CharField(max_length=1)
    transaccion_detalle = models.TextField()
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_fondeo = models.DateTimeField(auto_now_add=True)
    programa = models.ForeignKey(SistemaMunicipalPrograma, on_delete=models.CASCADE)

class ReglasOperacion(models.Model):
    regla = models.TextField()
    sexo = models.CharField(max_length=1)
    edad_inicio = models.IntegerField()
    edad_fin = models.IntegerField()
    colonia = models.CharField(max_length=1)
    municipal_programa = models.ForeignKey(SistemaMunicipalPrograma, on_delete=models.SET_NULL, null=True)

class Compromiso(models.Model):
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='compromisos_creados')
    promotor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='compromisos_apoyados')
    programa_social = models.ForeignKey(SistemaMunicipalPrograma, on_delete=models.SET_NULL, null=True, blank=True)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_compromiso_limite = models.DateField()
    fecha_verificacion = models.DateTimeField()
    monto = models.FloatField()
    monto_abonado = models.FloatField()
    agradecimiento_texto = models.TextField(blank=True, null=True)
    agradecimiento_imagen_path = models.TextField(blank=True, null=True)
    agradecimiento_video_path = models.TextField(blank=True, null=True)
    estatus = models.CharField(max_length=1)
    tipo = models.CharField(max_length=1)
    origen = models.CharField(max_length=1)

class CompromisoAbono(models.Model):
    compromiso = models.ForeignKey(Compromiso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=1)
    monto = models.FloatField()
    tipo_pago = models.CharField(max_length=1)

class CompromisoEvidencia(models.Model):
    archivo = models.CharField(max_length=255)
    fecha_carga = models.DateTimeField(auto_now_add=True)
    promotor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    compromiso = models.ForeignKey(Compromiso, on_delete=models.SET_NULL, null=True)

class Pregunta(models.Model):
    promotor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='preguntas_hechas')
    creador = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='preguntas_recibidas')
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=255)
    respuesta = models.CharField(max_length=255, blank=True, null=True)
    fecha_pregunta = models.DateField(auto_now_add=True)
    fecha_respuesta = models.DateField(blank=True, null=True)
    estatus = models.CharField(max_length=1)

class CatalogoWalletMovimiento(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Wallet(models.Model):
    id_morelia = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    saldo = models.FloatField(blank=True, null=True)
    fecha_actualizacion = models.DateField(auto_now=True)

class WalletMovimiento(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    tipo_movimiento = models.ForeignKey(CatalogoWalletMovimiento, on_delete=models.SET_NULL, null=True)
    monto = models.FloatField(blank=True, null=True)
    origen = models.CharField(max_length=255, blank=True, null=True)
    donacion = models.ForeignKey(CompromisoAbono, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

class SoporteMultimedia(models.Model):
    archivo_path = models.CharField(max_length=255, blank=True, null=True)
    fecha_carga = models.DateField(auto_now_add=True)
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)

class Configuracion(models.Model):
    clave = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)

class Chat(models.Model):
    from_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensajes_enviados')
    to_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    contenido = models.TextField()
    caso = models.ForeignKey(Caso, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
