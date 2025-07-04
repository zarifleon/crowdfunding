<template>
  <div class="pagina-crear-caso">
    <h2>Crear Nuevo Caso de Crowdfunding</h2>
    <form @submit.prevent="manejarCrearCaso" enctype="multipart/form-data" class="formulario-comun">

      <div class="form-grupo">
        <label for="creador_id_morelia">Tu ID Morelia (Creador):</label>
        <input type="text" id="creador_id_morelia" v-model="formData.creador_id_morelia" required class="form-control">
        <!-- En una app real, esto se tomaría del usuario autenticado, no se ingresaría manualmente -->
      </div>

      <div class="form-grupo">
        <label for="exposicion_titulo">Título del Caso:</label>
        <input type="text" id="exposicion_titulo" v-model="formData.exposicion_titulo" required class="form-control">
      </div>

      <div class="form-grupo">
        <label for="exposicion_quien_soy">¿Quién Soy? (Describe tu perfil o el de tu organización):</label>
        <textarea id="exposicion_quien_soy" v-model="formData.exposicion_quien_soy" rows="4" required class="form-control"></textarea>
      </div>

      <div class="form-grupo">
        <label for="exposicion_que_necesito">¿Qué Necesito? (Describe tu necesidad o proyecto):</label>
        <textarea id="exposicion_que_necesito" v-model="formData.exposicion_que_necesito" rows="4" required class="form-control"></textarea>
      </div>

      <div class="form-grupo">
        <label for="exposicion_porque">¿Por Qué? (Justifica la importancia de tu caso):</label>
        <textarea id="exposicion_porque" v-model="formData.exposicion_porque" rows="4" required class="form-control"></textarea>
      </div>

      <div class="form-grupo">
        <label for="exposicion_promocional">Texto Promocional (Resumen atractivo para tu caso):</label>
        <textarea id="exposicion_promocional" v-model="formData.exposicion_promocional" rows="3" required class="form-control"></textarea>
      </div>

      <div class="form-grupo">
        <label for="exposicion_detalles_adicionales">Detalles Adicionales (Opcional):</label>
        <textarea id="exposicion_detalles_adicionales" v-model="formData.exposicion_detalles_adicionales" rows="3" class="form-control"></textarea>
      </div>

      <div class="form-grupo">
        <label for="categoria_id">Categoría:</label>
        <select id="categoria_id" v-model="formData.categoria_id" required class="form-control">
          <option disabled value="">Selecciona una categoría</option>
          <option v-for="cat in categorias" :key="cat.id" :value="cat.id">{{ cat.nombre }}</option>
        </select>
        <div v-if="cargandoCategorias" class="info-carga-inline">Cargando categorías...</div>
      </div>

      <div class="form-grupo">
        <label for="cantidad_requerida">Cantidad Requerida (MXN):</label>
        <input type="number" id="cantidad_requerida" v-model.number="formData.cantidad_requerida" required min="1" step="0.01" class="form-control">
      </div>

      <div class="form-grupo">
        <label for="fecha_publicacion">Fecha de Publicación:</label>
        <input type="date" id="fecha_publicacion" v-model="formData.fecha_publicacion" required class="form-control">
      </div>

      <div class="form-grupo">
        <label for="fecha_fin">Fecha de Fin de Campaña:</label>
        <input type="date" id="fecha_fin" v-model="formData.fecha_fin" required :min="formData.fecha_publicacion" class="form-control">
      </div>

      <div class="form-grupo">
        <label for="imagen_promocional">Imagen Promocional (Opcional):</label>
        <input type="file" id="imagen_promocional" @change="manejarCambioArchivo($event, 'imagen_promocional')" accept="image/*" class="form-control">
        <img v-if="previsualizacionImagen" :src="previsualizacionImagen" alt="Previsualización de imagen" class="previsualizacion-archivo"/>
      </div>

      <div class="form-grupo">
        <label for="video_promocional">Video Promocional (Archivo de video, Opcional):</label>
        <input type="file" id="video_promocional" @change="manejarCambioArchivo($event, 'video_promocional')" accept="video/*" class="form-control">
        <!-- Nota: El backend espera un path o URL para video_promocional si no es FileField. Si es FileField, esto está bien. -->
        <!-- Mi backend actual lo tiene como FileField, así que esto es correcto. -->
      </div>

      <!-- Otros campos opcionales como estatus_id, programa_municipal_id podrían añadirse aquí -->

      <div v-if="errorApi" class="mensaje-error api-error">
        {{ errorApi }}
      </div>
      <div v-if="mensajeExito" class="mensaje-exito api-exito">
        {{ mensajeExito }}
      </div>

      <button type="submit" :disabled="cargando" class="boton boton-primario">
        {{ cargando ? 'Creando Caso...' : 'Crear Caso' }}
      </button>
    </form>
  </div>
</template>

<script>
const API_BASE_URL = '/api/v1/crowdfunding';

export default {
  name: 'PaginaCrearCaso',
  data() {
    return {
      formData: {
        creador_id_morelia: '', // TEMPORAL: Debería ser tomado del usuario autenticado
        exposicion_titulo: '',
        exposicion_quien_soy: '',
        exposicion_que_necesito: '',
        exposicion_porque: '',
        exposicion_promocional: '',
        exposicion_detalles_adicionales: '',
        categoria_id: '',
        cantidad_requerida: null,
        fecha_publicacion: new Date().toISOString().split('T')[0], // Default a hoy
        fecha_fin: '',
        // Los archivos se manejarán por separado en el objeto FormData para el envío
      },
      archivoImagen: null,
      previsualizacionImagen: null,
      archivoVideo: null,
      categorias: [],
      cargandoCategorias: false,
      cargando: false,
      errorApi: null,
      mensajeExito: null,
    };
  },
  methods: {
    async fetchCategorias() {
      this.cargandoCategorias = true;
      try {
        // Asumiendo que tenemos un endpoint para listar categorías (no implementado aún en backend)
        // Por ahora, simularemos o dejaremos vacío. Si el endpoint existiera:
        // const response = await fetch(`${API_BASE_URL}/catalogos/categorias/`);
        // if (!response.ok) throw new Error('Error al cargar categorías');
        // this.categorias = await response.json();

        // Simulación de categorías:
        this.categorias = [
          { id: 1, nombre: 'Salud y Bienestar' },
          { id: 2, nombre: 'Educación' },
          { id: 3, nombre: 'Emprendimiento' },
          { id: 4, nombre: 'Arte y Cultura' },
          { id: 5, nombre: 'Medio Ambiente' },
          { id: 6, nombre: 'Comunitario' },
        ];
      } catch (error) {
        console.error("Error fetching categorías:", error);
        // Manejar error de carga de categorías
      } finally {
        this.cargandoCategorias = false;
      }
    },
    manejarCambioArchivo(event, tipo) {
      const file = event.target.files[0];
      if (!file) {
        if (tipo === 'imagen_promocional') {
          this.archivoImagen = null;
          this.previsualizacionImagen = null;
        } else if (tipo === 'video_promocional') {
          this.archivoVideo = null;
        }
        return;
      }

      if (tipo === 'imagen_promocional') {
        this.archivoImagen = file;
        // Previsualización de imagen
        const reader = new FileReader();
        reader.onload = (e) => {
          this.previsualizacionImagen = e.target.result;
        };
        reader.readAsDataURL(file);
      } else if (tipo === 'video_promocional') {
        this.archivoVideo = file;
      }
    },
    async manejarCrearCaso() {
      this.cargando = true;
      this.errorApi = null;
      this.mensajeExito = null;

      // Validar fecha_fin > fecha_publicacion
      if (new Date(this.formData.fecha_fin) <= new Date(this.formData.fecha_publicacion)) {
          this.errorApi = "La fecha de fin de campaña debe ser posterior a la fecha de publicación.";
          this.cargando = false;
          return;
      }

      const formDataPayload = new FormData();
      // Añadir campos de texto
      for (const key in this.formData) {
        if (this.formData[key] !== null && this.formData[key] !== undefined) {
           formDataPayload.append(key, this.formData[key]);
        }
      }
      // Añadir archivos
      if (this.archivoImagen) {
        formDataPayload.append('imagen_promocional', this.archivoImagen, this.archivoImagen.name);
      }
      if (this.archivoVideo) {
        formDataPayload.append('video_promocional', this.archivoVideo, this.archivoVideo.name);
      }
      // Aquí también se podrían añadir estatus_id, programa_municipal_id si se recolectan

      try {
        const response = await fetch(`${API_BASE_URL}/casos/crear/`, {
          method: 'POST',
          body: formDataPayload, // FormData se envía sin 'Content-Type' explícito, el navegador lo pone.
          // CSRF token si es necesario
        });

        // Como la respuesta puede no ser JSON si hay un error de servidor antes de procesar la solicitud (ej. 413 Payload Too Large)
        // es mejor verificar el content-type o intentar parsear y capturar el error.
        let responseData;
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
            responseData = await response.json();
        } else {
            // Si no es JSON, podría ser un error HTML o de texto plano del servidor/proxy
            if (!response.ok) {
                 this.errorApi = `Error ${response.status}: ${response.statusText || 'Error desconocido del servidor.'}`;
                 this.cargando = false;
                 return;
            }
            // Si es OK pero no JSON, es inesperado.
            responseData = { mensaje: "Operación completada, pero respuesta no es JSON." };
        }

        if (!response.ok) {
          this.errorApi = responseData.error || `Error ${response.status}: ${responseData.detail || response.statusText}`;
        } else {
          this.mensajeExito = `Caso "${responseData.caso_id ? this.formData.exposicion_titulo : ''}" creado exitosamente (ID: ${responseData.caso_id}).`;
          // Limpiar formulario y opcionalmente redirigir
          this.formData = { /* ...valores iniciales... */ };
          this.archivoImagen = null; this.previsualizacionImagen = null; this.archivoVideo = null;
          // this.$router.push(`/casos/${responseData.caso_id}`); // Redirigir al detalle del caso
        }
      } catch (error) {
        console.error("Error al crear caso:", error);
        this.errorApi = "No se pudo conectar con el servidor o error en la solicitud. Intenta de nuevo.";
      } finally {
        this.cargando = false;
      }
    }
  },
  created() {
    this.fetchCategorias();
    // En una app real, el ID del creador vendría del store de autenticación
    // this.formData.creador_id_morelia = this.$store.state.auth.usuario.id_morelia;
  }
}
</script>

<style scoped>
.pagina-crear-caso {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.pagina-crear-caso h2 {
  text-align: center;
  color: #333;
  margin-bottom: 2rem;
}
.previsualizacion-archivo {
  max-width: 200px;
  max-height: 200px;
  margin-top: 10px;
  border: 1px solid #ddd;
  padding: 5px;
}
.info-carga-inline {
    font-size: 0.8em;
    color: #6c757d;
}
.api-error, .api-exito {
  margin-top: 1rem; /* Para separarlo del último campo */
  margin-bottom: 1rem;
  padding: 0.75rem;
  border-radius: 4px;
  text-align: center;
}
.api-error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}
.api-exito {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}
.boton {
  width: 100%;
  margin-top: 1.5rem;
}
</style>
