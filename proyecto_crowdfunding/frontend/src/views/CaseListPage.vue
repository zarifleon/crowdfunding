<template>
  <div class="case-list-page"> <!-- Renamed class -->
    <header class="page-header"> <!-- Renamed class -->
      <h1>Explora Todos los Casos</h1>
      <p>Encuentra proyectos que te inspiren y apóyalos.</p>
    </header>

    <div v-if="loading" class="loading-message"> <!-- Renamed data prop, class -->
      Cargando casos...
    </div>
    <div v-if="error" class="error-message"> <!-- Renamed data prop, class -->
      Error al cargar los casos: {{ error }}
    </div>

    <div class="filters-and-sort" v-if="!loading && !error && cases.length"> <!-- Renamed class, data prop -->
      <p>Filtros y ordenación (próximamente)</p>
    </div>

    <div class="case-grid" v-if="!loading && !error && cases.length"> <!-- Renamed class, data prop -->
      <CaseCard v-for="caseItem in cases" :key="caseItem.id" :caseItem="mapCaseData(caseItem)" /> <!-- Renamed component, prop -->
    </div>

    <div v-if="!loading && !error && !cases.length" class="empty-message"> <!-- Renamed data prop, class -->
      Actualmente no hay casos publicados. ¡Intenta de nuevo más tarde!
    </div>

    <div class="pagination-controls" v-if="!loading && !error && cases.length > 10"> <!-- Renamed class, data prop -->
        <p>Paginación (próximamente)</p>
    </div>
  </div>
</template>

<script>
import CaseCard from '../components/CaseCard.vue';
import { mockCases } from '../mock_data/cases.js'; // Import mock data

const API_BASE_URL = '/api/v1/crowdfunding';
const USE_MOCK_DATA = true; // Switch for using mock data

export default {
  name: 'CaseListPage',
  components: {
    CaseCard
  },
  data() {
    return {
      cases: [],
      loading: false,
      error: null,
    };
  },
  methods: {
    async fetchAllCases() {
      this.loading = true;
      this.error = null;
      if (USE_MOCK_DATA) {
        console.log("CaseListPage: Using MOCK data for all cases.");
        this.cases = mockCases; // Use all mock cases
        this.loading = false;
      } else {
        console.log("CaseListPage: Fetching all cases from API.");
        try {
          const response = await fetch(`${API_BASE_URL}/casos/`);
          if (!response.ok) {
            throw new Error(`Server error: ${response.status} ${response.statusText}`);
          }
          this.cases = await response.json();
        } catch (err) {
          console.error("Error fetching all cases:", err);
          this.error = err.message;
        } finally {
          this.loading = false;
        }
      }
    },
    mapCaseData(apiCase) {
      let imageUrl = '';
      const mediaUrlBase = '/media/';
      if (apiCase.imagen_promocional) {
        // Assumes imagen_promocional in mock data is now like "casos_imagenes/file.jpg"
        imageUrl = `${mediaUrlBase}${apiCase.imagen_promocional}`;
      }

      return {
        const mediaUrlBase = '/media/';
        imageUrl = `${mediaUrlBase}${apiCase.imagen_promocional}`;
      }

      return { // Maps to caseItem prop of CaseCard
        id: apiCase.id,
        titulo: apiCase.titulo,
        creador_nombre_completo: apiCase.creador ? apiCase.creador.nombre_completo : (apiCase.creador_id || 'N/A'),
        creador_id: apiCase.creador ? apiCase.creador.id_morelia : (apiCase.creador_id || 'N/A'),
        quien_soy: apiCase.quien_soy,
        imagen_promocional_url: imageUrl,
        cantidad_obtenida: apiCase.cantidad_obtenida,
        cantidad_requerida: apiCase.cantidad_requerida,
        estatus_nombre: apiCase.estatus || 'Undefined',
      };
    }
  },
  created() {
    this.fetchAllCases(); // Renamed method
  }
}
</script>

<style scoped>
.case-list-page { /* Renamed class */
  padding: 1rem;
}

.page-header { /* Renamed class */
  background-color: #f8f9fa;
  padding: 2rem 1rem;
  margin-bottom: 2rem;
  border-radius: 8px;
  text-align: center;
}

.page-header h1 { /* Renamed class */
  font-size: 2.2rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.page-header p { /* Renamed class */
  font-size: 1.1rem;
  color: #6c757d;
}

.filters-and-sort { /* Renamed class */
  margin-bottom: 1.5rem;
  padding: 1rem;
  background-color: #fff;
  border-radius: 6px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  text-align: center;
}

.case-grid { /* Renamed class */
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.loading-message, .error-message, .empty-message { /* Renamed classes */
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
  color: #555;
}
.error-message { /* Renamed class */
  color: #dc3545;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  border-radius: 4px;
}
.empty-message { /* Renamed class */
  background-color: #e9ecef;
  border-radius: 4px;
}

.pagination-controls { /* Renamed class */
  margin-top: 2rem;
  text-align: center;
  padding: 1rem;
  background-color: #fff;
  border-radius: 6px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
</style>
