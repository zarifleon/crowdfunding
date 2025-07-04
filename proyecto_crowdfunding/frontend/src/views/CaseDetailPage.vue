<template>
  <div class="case-detail-page" v-if="caseData"> <!-- Renamed class, data prop -->
    <header class="case-detail-header"> <!-- Renamed class -->
      <h1>{{ caseData.titulo }}</h1> <!-- Renamed data prop -->
      <p class="creator-subtitle"> <!-- Renamed class -->
        Inciativa de: <strong>{{ caseData.creador ? caseData.creador.nombre_completo : 'Desconocido' }}</strong> <!-- Renamed data prop -->
      </p>
      <div class="meta-info">
        <span>Categoría: {{ caseData.categoria || 'No especificada' }}</span> <!-- Renamed data prop -->
        <span>Estatus: {{ caseData.estatus || 'No definido' }}</span> <!-- Renamed data prop -->
        <span>Publicado: {{ formatDate(caseData.fecha_publicacion) }}</span> <!-- Renamed method, data prop -->
        <span>Finaliza: {{ formatDate(caseData.fecha_fin) }}</span> <!-- Renamed method, data prop -->
      </div>
    </header>

    <div class="case-detail-body"> <!-- Renamed class -->
      <div class="main-column"> <!-- Renamed class -->
        <img v-if="caseData.imagen_promocional_url" :src="caseData.imagen_promocional_url" :alt="'Imagen de ' + caseData.titulo" class="main-case-image"> <!-- Renamed data prop, class -->

        <section class="description-section"> <!-- Renamed class -->
          <h3>¿Quién Soy?</h3>
          <p>{{ caseData.quien_soy }}</p> <!-- Renamed data prop -->
          <h3>¿Qué Necesito?</h3>
          <p>{{ caseData.que_necesito }}</p> <!-- Renamed data prop -->
          <h3>¿Por Qué?</h3>
          <p>{{ caseData.porque }}</p> <!-- Renamed data prop -->
          <div v-if="caseData.detalles_adicionales"> <!-- Renamed data prop -->
            <h3>Detalles Adicionales</h3>
            <p>{{ caseData.detalles_adicionales }}</p> <!-- Renamed data prop -->
          </div>
        </section>

        <section class="video-section" v-if="caseData.video_promocional_url"> <!-- Renamed class, data prop -->
          <h3>Video Promocional</h3>
          <iframe width="560" height="315" :src="caseData.video_promocional_url" frameborder="0" allowfullscreen></iframe> <!-- Renamed data prop -->
        </section>

        <section class="articles-section" v-if="caseData.articulos && caseData.articulos.length"> <!-- Renamed class, data prop -->
            <h3>Artículos/Necesidades Específicas</h3>
            <ul>
                <li v-for="articulo in caseData.articulos" :key="articulo.id"> <!-- Renamed data prop -->
                    <strong>{{ articulo.descripcion }}</strong> - {{ formatCurrency(articulo.precio) }} (Recibo: {{ articulo.recibo_tipo }}) <!-- Renamed method -->
                </li>
            </ul>
        </section>

      </div>

      <aside class="sidebar-column"> <!-- Renamed class -->
        <div class="funding-panel"> <!-- Renamed class -->
          <h3>Apoya este Caso</h3>
          <div class="funding-progress"> <!-- Renamed class -->
            <div class="progress-bar-detail" :style="{ width: percentageFunded + '%' }"> <!-- Renamed class, computed prop -->
              {{ percentageFunded.toFixed(0) }}%
            </div>
          </div>
          <p class="amounts"> <!-- Renamed class -->
            <strong>{{ formatCurrency(caseData.cantidad_obtenida) }}</strong> recaudado de <!-- Renamed method, data prop -->
            <span>{{ formatCurrency(caseData.cantidad_requerida) }}</span> <!-- Renamed method, data prop -->
          </p>
          <button class="button button-primary button-large support-button">Quiero Apoyar</button> <!-- Renamed class -->
          <button class="button button-secondary share-button">Compartir</button> <!-- Renamed class -->
        </div>
        <div class="creator-panel" v-if="caseData.creador"> <!-- Renamed class, data prop -->
          <h4>Sobre el Creador</h4>
          <p><strong>{{ caseData.creador.nombre_completo }}</strong></p> <!-- Renamed data prop -->
          <p>ID Morelia: {{ caseData.creador.id_morelia }}</p> <!-- Renamed data prop -->
          <p>Email: {{ caseData.creador.email }}</p> <!-- Renamed data prop -->
        </div>
      </aside>
    </div>

    <section class="interaction-section"> <!-- Renamed class -->
        <h3>Preguntas y Respuestas</h3>
        <p>(Próximamente)</p>
        <h3>Actualizaciones del Proyecto</h3>
        <p>(Próximamente)</p>
    </section>

  </div>
  <div v-if="loading" class="loading-message">Cargando detalles del caso...</div> <!-- Renamed data prop, class -->
  <div v-if="error" class="error-message">Error al cargar el caso: {{ error }}</div> <!-- Renamed data prop, class -->
</template>

<script>
import { getMockCaseById } from '../mock_data/cases.js'; // Import mock data helper

const API_BASE_URL = '/api/v1/crowdfunding';
const MEDIA_URL_BASE = '/media/';
const USE_MOCK_DATA = true; // Switch for using mock data

export default {
  name: 'CaseDetailPage',
  props: ['caseId'],
  data() {
    return {
      caseData: null,
      loading: false,
      error: null,
    };
  },
  computed: {
    percentageFunded() {
      if (!this.caseData || !this.caseData.cantidad_requerida || this.caseData.cantidad_requerida === 0) {
        return 0;
      }
      const percentage = (this.caseData.cantidad_obtenida / this.caseData.cantidad_requerida) * 100;
      return Math.min(percentage, 100);
    }
  },
  methods: {
    async fetchCaseDetails() { // Renamed method
      this.loading = true;
      this.error = null;
      try {
        const response = await fetch(`${API_BASE_URL}/casos/${this.caseId}/`);
        if (!response.ok) {
          if (response.status === 404) {
            throw new Error('Caso no encontrado.');
          }
          throw new Error(`Server error: ${response.status} ${response.statusText}`);
        }
        const apiCase = await response.json();
        this.caseData = this.mapApiDataToLocal(apiCase); // Renamed data prop

      } catch (err) { // Renamed error variable
        console.error(`Error fetching case details for ${this.caseId}:`, err); // Anglicized log
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    },
    mapApiDataToLocal(apiCase) {
      let imageUrl = '';
      if (apiCase.imagen_promocional) {
        imageUrl = `${MEDIA_URL_BASE}${apiCase.imagen_promocional}`;
      }

      return {
        ...apiCase,
        imagen_promocional_url: imageUrl,
        video_promocional_url: apiCase.video_promocional,
        categoria: apiCase.categoria,
        estatus: apiCase.estatus,
      };
    },
    formatCurrency(value) { // Renamed method
      if (typeof value !== 'number') {
        value = parseFloat(value) || 0;
      }
      return `$${value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}`;
    },
    formatDate(isoDate) { // Renamed method
      if (!isoDate) return 'N/A';
      try {
        const date = new Date(isoDate);
        return date.toLocaleDateString('es-MX', { year: 'numeric', month: 'long', day: 'numeric' });
      } catch (e) {
        return isoDate;
      }
    }
  },
  created() {
    if (this.caseId) {
      this.fetchCaseDetails(); // Renamed method
    } else {
      this.error = "No case ID specified."; // Anglicized message
    }
  },
}
</script>

<style scoped>
.case-detail-page { /* Renamed class */
  max-width: 1000px;
  margin: 1rem auto;
  padding: 1rem;
}

.case-detail-header { /* Renamed class */
  background-color: #e9ecef;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  text-align: left;
}
.case-detail-header h1 { /* Renamed class */
  font-size: 2.3rem;
  color: #2c3e50;
  margin-top: 0;
  margin-bottom: 0.5rem;
}
.creator-subtitle { /* Renamed class */
  font-size: 1.1rem;
  color: #495057;
  margin-bottom: 1rem;
}
.meta-info {
  font-size: 0.9rem;
  color: #6c757d;
}
.meta-info span {
  margin-right: 1.5rem;
}
.meta-info span:last-child {
  margin-right: 0;
}

.case-detail-body { /* Renamed class */
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
}

.main-column { /* Renamed class */
  flex: 3;
  min-width: 300px;
}

.main-case-image { /* Renamed class */
  width: 100%;
  max-height: 450px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  background-color: #f0f0f0;
}

.description-section h3, .video-section h3, .articles-section h3, .interaction-section h3 { /* Renamed classes */
  font-size: 1.5rem;
  color: #0056b3;
  margin-top: 2rem;
  margin-bottom: 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #007bff;
}
.description-section p { /* Renamed class */
  line-height: 1.7;
  margin-bottom: 1rem;
}
.articles-section ul { /* Renamed class */
    list-style: disc;
    padding-left: 20px;
}
.articles-section li { /* Renamed class */
    margin-bottom: 0.5rem;
}

.video-section iframe { /* Renamed class */
    max-width: 100%;
    border-radius: 8px;
}

.sidebar-column { /* Renamed class */
  flex: 1;
  min-width: 280px;
}

.funding-panel, .creator-panel { /* Renamed classes */
  background-color: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}
.funding-panel h3, .creator-panel h4 { /* Renamed classes */
  margin-top: 0;
  color: #343a40;
}
.funding-progress { /* Renamed class */
  background-color: #e0e0e0;
  border-radius: 20px;
  height: 25px;
  margin-bottom: 0.75rem;
  overflow: hidden;
  position: relative;
}
.progress-bar-detail { /* Renamed class */
  background-color: #28a745;
  height: 100%;
  transition: width 0.5s ease;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 0.9rem;
}
.amounts { /* Renamed class */
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}
.amounts strong { /* Renamed class */
  color: #28a745;
  font-size: 1.5rem;
}
.amounts span { /* Renamed class */
    font-size: 1rem;
    color: #6c757d;
}
.support-button { /* Renamed class */
  width: 100%;
  margin-bottom: 0.75rem;
}
.share-button { /* Renamed class */
  width: 100%;
}

.creator-panel p { /* Renamed class */
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
}

.interaction-section { /* Renamed class */
    margin-top: 3rem;
    padding: 1.5rem;
    background-color: #fff;
    border-radius: 8px;
}

.loading-message, .error-message { /* Renamed classes */
  padding: 1rem;
  text-align: center;
}
</style>
