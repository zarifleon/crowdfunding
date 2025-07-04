<template>
  <div class="create-case-page"> <!-- Renamed class -->
    <h2>Crear Nuevo Caso de Crowdfunding</h2>
    <form @submit.prevent="handleCreateCase" enctype="multipart/form-data" class="common-form"> <!-- Renamed method, class -->

      <div class="form-group"> <!-- Renamed class -->
        <label for="creador_id_morelia">Tu ID Morelia (Creador):</label>
        <input type="text" id="creador_id_morelia" v-model="formData.creador_id_morelia" required class="form-control">
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="exposicion_titulo">Título del Caso:</label>
        <input type="text" id="exposicion_titulo" v-model="formData.exposicion_titulo" required class="form-control">
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="exposicion_quien_soy">¿Quién Soy? (Describe tu perfil o el de tu organización):</label>
        <textarea id="exposicion_quien_soy" v-model="formData.exposicion_quien_soy" rows="4" required class="form-control"></textarea>
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="exposicion_que_necesito">¿Qué Necesito? (Describe tu necesidad o proyecto):</label>
        <textarea id="exposicion_que_necesito" v-model="formData.exposicion_que_necesito" rows="4" required class="form-control"></textarea>
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="exposicion_porque">¿Por Qué? (Justifica la importancia de tu caso):</label>
        <textarea id="exposicion_porque" v-model="formData.exposicion_porque" rows="4" required class="form-control"></textarea>
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="exposicion_promocional">Texto Promocional (Resumen atractivo para tu caso):</label>
        <textarea id="exposicion_promocional" v-model="formData.exposicion_promocional" rows="3" required class="form-control"></textarea>
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="exposicion_detalles_adicionales">Detalles Adicionales (Opcional):</label>
        <textarea id="exposicion_detalles_adicionales" v-model="formData.exposicion_detalles_adicionales" rows="3" class="form-control"></textarea>
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="categoria_id">Categoría:</label>
        <select id="categoria_id" v-model="formData.categoria_id" required class="form-control">
          <option disabled value="">Selecciona una categoría</option>
          <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.nombre }}</option> <!-- Renamed data prop -->
        </select>
        <div v-if="loadingCategories" class="inline-loading-info">Cargando categorías...</div> <!-- Renamed data prop, class -->
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="cantidad_requerida">Cantidad Requerida (MXN):</label>
        <input type="number" id="cantidad_requerida" v-model.number="formData.cantidad_requerida" required min="1" step="0.01" class="form-control">
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="fecha_publicacion">Fecha de Publicación:</label>
        <input type="date" id="fecha_publicacion" v-model="formData.fecha_publicacion" required class="form-control">
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="fecha_fin">Fecha de Fin de Campaña:</label>
        <input type="date" id="fecha_fin" v-model="formData.fecha_fin" required :min="formData.fecha_publicacion" class="form-control">
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="imagen_promocional">Imagen Promocional (Opcional):</label>
        <input type="file" id="imagen_promocional" @change="handleFileChange($event, 'image')" accept="image/*" class="form-control"> <!-- Renamed method, type -->
        <img v-if="imagePreview" :src="imagePreview" alt="Previsualización de imagen" class="file-preview"/> <!-- Renamed data prop, class -->
      </div>

      <div class="form-group"> <!-- Renamed class -->
        <label for="video_promocional">Video Promocional (Archivo de video, Opcional):</label>
        <input type="file" id="video_promocional" @change="handleFileChange($event, 'video')" accept="video/*" class="form-control"> <!-- Renamed method, type -->
      </div>

      <div v-if="apiError" class="error-message api-feedback-error"> <!-- Renamed data prop, class -->
        {{ apiError }}
      </div>
      <div v-if="successMessage" class="success-message api-feedback-success"> <!-- Renamed data prop, class -->
        {{ successMessage }}
      </div>

      <button type="submit" :disabled="loading" class="button button-primary"> <!-- Renamed data prop, class -->
        {{ loading ? 'Creando Caso...' : 'Crear Caso' }}
      </button>
    </form>
  </div>
</template>

<script>
import { mockCategories } from '../mock_data/cases.js'; // Import mock categories

const API_BASE_URL = '/api/v1/crowdfunding';
const USE_MOCK_DATA_FOR_CATALOGS = true; // Switch for catalog data

export default {
  name: 'CreateCasePage',
  data() {
    return {
      formData: {
        creador_id_morelia: '',
        exposicion_titulo: '',
        exposicion_quien_soy: '',
        exposicion_que_necesito: '',
        exposicion_porque: '',
        exposicion_promocional: '',
        exposicion_detalles_adicionales: '',
        categoria_id: '',
        cantidad_requerida: null,
        fecha_publicacion: new Date().toISOString().split('T')[0],
        fecha_fin: '',
      },
      imageFile: null, // Renamed
      imagePreview: null, // Renamed
      videoFile: null, // Renamed
      categories: [], // Renamed
      loadingCategories: false, // Renamed
      loading: false, // Renamed
      apiError: null, // Renamed
      successMessage: null, // Renamed
    };
  },
  methods: {
    async fetchCategories() { // Renamed method
      this.loadingCategories = true;
      try {
        // Actual API call would go here
        this.categories = [
          { id: 1, nombre: 'Salud y Bienestar' }, { id: 2, nombre: 'Educación' },
          { id: 3, nombre: 'Emprendimiento' }, { id: 4, nombre: 'Arte y Cultura' },
          { id: 5, nombre: 'Medio Ambiente' }, { id: 6, nombre: 'Comunitario' },
        ];
      } catch (error) {
        console.error("Error fetching categories:", error); // Anglicized log
      } finally {
        this.loadingCategories = false;
      }
    },
    handleFileChange(event, fileType) { // Renamed method, param
      const file = event.target.files[0];
      if (!file) {
        if (fileType === 'image') {
          this.imageFile = null;
          this.imagePreview = null;
        } else if (fileType === 'video') {
          this.videoFile = null;
        }
        return;
      }

      if (fileType === 'image') {
        this.imageFile = file;
        const reader = new FileReader();
        reader.onload = (e) => { this.imagePreview = e.target.result; };
        reader.readAsDataURL(file);
      } else if (fileType === 'video') {
        this.videoFile = file;
      }
    },
    async handleCreateCase() { // Renamed method
      this.loading = true;
      this.apiError = null;
      this.successMessage = null;

      if (new Date(this.formData.fecha_fin) <= new Date(this.formData.fecha_publicacion)) {
          this.apiError = "La fecha de fin de campaña debe ser posterior a la fecha de publicación.";
          this.loading = false;
          return;
      }

      const formDataPayload = new FormData();
      for (const key in this.formData) {
        if (this.formData[key] !== null && this.formData[key] !== undefined) {
           formDataPayload.append(key, this.formData[key]);
        }
      }
      if (this.imageFile) {
        formDataPayload.append('imagen_promocional', this.imageFile, this.imageFile.name);
      }
      if (this.videoFile) {
        formDataPayload.append('video_promocional', this.videoFile, this.videoFile.name);
      }

      try {
        const response = await fetch(`${API_BASE_URL}/casos/crear/`, {
          method: 'POST',
          body: formDataPayload,
        });

        let responseData;
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
            responseData = await response.json();
        } else {
            if (!response.ok) {
                 this.apiError = `Error ${response.status}: ${response.statusText || 'Unknown server error.'}`; // Anglicized
                 this.loading = false;
                 return;
            }
            responseData = { mensaje: "Operation completed, but response was not JSON." }; // Anglicized
        }

        if (!response.ok) {
          this.apiError = responseData.error || `Error ${response.status}: ${responseData.detail || response.statusText}`;
        } else {
          this.successMessage = `Caso "${responseData.caso_id ? this.formData.exposicion_titulo : ''}" creado exitosamente (ID: ${responseData.caso_id}).`;
          this.formData = { /* reset form */ };
          this.imageFile = null; this.imagePreview = null; this.videoFile = null;
          // this.$router.push(`/cases/${responseData.caso_id}`); // Updated path
        }
      } catch (error) {
        console.error("Error creating case:", error); // Anglicized log
        this.apiError = "Could not connect to server or request error. Please try again."; // Anglicized
      } finally {
        this.loading = false;
      }
    }
  },
  created() {
    this.fetchCategories(); // Renamed
  }
}
</script>

<style scoped>
.create-case-page { /* Renamed class */
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.create-case-page h2 { /* Renamed class */
  text-align: center;
  color: #333;
  margin-bottom: 2rem;
}
.file-preview { /* Renamed class */
  max-width: 200px;
  max-height: 200px;
  margin-top: 10px;
  border: 1px solid #ddd;
  padding: 5px;
}
.inline-loading-info { /* Renamed class */
    font-size: 0.8em;
    color: #6c757d;
}
.api-feedback-error, .api-feedback-success { /* Renamed classes */
  margin-top: 1rem;
  margin-bottom: 1rem;
  padding: 0.75rem;
  border-radius: 4px;
  text-align: center;
}
.api-feedback-error { /* Renamed class */
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}
.api-feedback-success { /* Renamed class */
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}
.button { /* Global style assumed */
  width: 100%;
  margin-top: 1.5rem;
}
</style>
