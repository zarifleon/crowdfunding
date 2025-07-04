<template>
  <div class="home-page"> <!-- Renamed class -->
    <header class="hero-header"> <!-- Renamed class -->
      <h1>Encuentra y Apoya Proyectos Locales</h1>
      <p>Tu contribución puede hacer la diferencia en Morelia.</p>
      <router-link to="/cases" class="button button-primary button-large">Explorar Casos</router-link> <!-- Renamed class, path -->
    </header>

    <section class="featured-cases-section"> <!-- Renamed class -->
      <h2>Casos Destacados</h2>
      <div v-if="loadingCases" class="loading-message"> <!-- Renamed data prop -->
        Cargando casos...
      </div>
      <div v-if="errorCases" class="error-message"> <!-- Renamed data prop -->
        Error al cargar los casos: {{ errorCases }}
      </div>
      <div class="case-list" v-if="!loadingCases && !errorCases && featuredCases.length"> <!-- Renamed class, data prop -->
        <CaseCard v-for="caseItem in featuredCases" :key="caseItem.id" :caseItem="mapCaseData(caseItem)" /> <!-- Renamed component, prop -->
      </div>
      <div v-if="!loadingCases && !errorCases && !featuredCases.length" class="empty-message"> <!-- Renamed data prop -->
        No hay casos destacados en este momento. ¡Vuelve pronto!
      </div>
    </section>

    <section class="how-it-works-section"> <!-- Renamed class -->
      <h2>¿Cómo Funciona?</h2>
      <div class="how-it-works-steps"> <!-- Renamed class -->
        <div class="step"> <!-- Renamed class -->
          <span class="step-icon">1</span> <!-- Renamed class -->
          <h3>Registra tu Idea</h3>
          <p>Presenta tu proyecto o necesidad a la comunidad.</p>
        </div>
        <div class="step"> <!-- Renamed class -->
          <span class="step-icon">2</span> <!-- Renamed class -->
          <h3>Recibe Apoyo</h3>
          <p>Ciudadanos y empresas pueden aportar a tu causa.</p>
        </div>
        <div class="step"> <!-- Renamed class -->
          <span class="step-icon">3</span> <!-- Renamed class -->
          <h3>Hazlo Realidad</h3>
          <p>Utiliza los fondos para concretar tu proyecto y muestra tus avances.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import CaseCard from '../components/CaseCard.vue';
import { mockCases } from '../mock_data/cases.js'; // Import mock data

const API_BASE_URL = '/api/v1/crowdfunding';
const USE_MOCK_DATA = true; // Switch to true to use mock data, false for API

export default {
  name: 'HomePage',
  components: {
    CaseCard
  },
  data() {
    return {
      featuredCases: [],
      loadingCases: false,
      errorCases: null,
    };
  },
  methods: {
    async fetchFeaturedCases() {
      this.loadingCases = true;
      this.errorCases = null;
      if (USE_MOCK_DATA) {
        console.log("HomePage: Using MOCK data for featured cases.");
        this.featuredCases = mockCases.slice(0, 3); // Take first 3 as featured
        this.loadingCases = false;
      } else {
        console.log("HomePage: Fetching featured cases from API.");
        try {
          const response = await fetch(`${API_BASE_URL}/casos/`);
          if (!response.ok) {
            throw new Error(`Server error: ${response.status} ${response.statusText}`);
          }
          const allCases = await response.json();
          this.featuredCases = allCases.slice(0, 3);
        } catch (error) {
          console.error("Error fetching featured cases:", error);
          this.errorCases = error.message;
        } finally {
          this.loadingCases = false;
        }
      }
    },
    mapCaseData(apiCase) {
      // This mapping is now important for both API and mock data to align with CaseCard prop expectation
      let imageUrl = '';
      if (apiCase.imagen_promocional) {
        // For mock data, imagen_promocional is a relative path like "sample_images/comedor_esperanza.jpg"
        // For real API, it's just the filename part: "comedor_esperanza.jpg"
        // The '/media/' prefix is needed for both to simulate how Django serves media.
        // A more robust solution would involve environment variables for base URLs.
        const mediaUrlBase = '/media/';
        if (USE_MOCK_DATA && apiCase.imagen_promocional.startsWith('sample_images/')) {
            // For mock data, we might need a different base if images are locally served differently
            // For this simulation, we assume it's also relative to where /media/ would point.
            // Or, provide full URLs in mock data if easier.
            // For now, let's assume the structure is just the filename for consistency with backend.
            // So, mock data should just have "comedor_esperanza.jpg"
            // Let's adjust the mock data or this logic.
            // For simplicity, I'll assume mock data provides just the filename for now, like the API.
            // OR, if mock data has full path, then:
             // if (apiCase.imagen_promocional.startsWith('http')) imageUrl = apiCase.imagen_promocional;
             // else imageUrl = `${mediaUrlBase}${apiCase.imagen_promocional}`;
            // Let's assume for mock data, we might have a placeholder or need to adjust.
            // The current mock data has "sample_images/..." which is not ideal.
            // I will assume `apiCase.imagen_promocional` from mock data is just the filename part
            // and the `mediaUrlBase` is always prepended.
            // For a quick fix, I'll adjust the mock data to just have filenames.
            // (Will do that in a separate step for the mock_data file itself if needed, for now, this logic)

            // If mock data has "sample_images/file.jpg" and API has "file.jpg"
            // and both need "/media/" + "actual_path_in_media_root"
            // The current backend provides "casos_imagenes/file.jpg"
            // So, the mock data should also reflect this, e.g. "casos_imagenes/comedor_esperanza.jpg"
            // Then the logic is simply:
            if (apiCase.imagen_promocional) {
                 imageUrl = `${mediaUrlBase}${apiCase.imagen_promocional}`;
            }
        } else if (apiCase.imagen_promocional) { // From Real API
            imageUrl = `${mediaUrlBase}${apiCase.imagen_promocional}`;
        }
      }

      return {
        id: apiCase.id,
        titulo: apiCase.titulo,
        creador_nombre_completo: apiCase.creador ? apiCase.creador.nombre_completo : 'N/A',
        creador_id: apiCase.creador ? apiCase.creador.id_morelia : 'N/A',
        quien_soy: apiCase.quien_soy,
        imagen_promocional_url: imageUrl, // This is the crucial part
        cantidad_obtenida: apiCase.cantidad_obtenida,
        cantidad_requerida: apiCase.cantidad_requerida,
        estatus_nombre: apiCase.estatus || 'Undefined', // Mock data provides 'estatus', API provides 'estatus.nombre'
                                                    // Let's ensure consistency. API provides estatus name.
      };
    }
  },
  created() {
        const mediaUrlBase = '/media/';
        imageUrl = `${mediaUrlBase}${apiCase.imagen_promocional}`;
      }

      return { // This maps to the 'caseItem' prop of CaseCard.vue
        id: apiCase.id,
        titulo: apiCase.titulo,
        creador_nombre_completo: apiCase.creador ? apiCase.creador.nombre_completo : 'N/A',
        creador_id: apiCase.creador ? apiCase.creador.id_morelia : 'N/A',
        quien_soy: apiCase.quien_soy,
        imagen_promocional_url: imageUrl,
        cantidad_obtenida: apiCase.cantidad_obtenida,
        cantidad_requerida: apiCase.cantidad_requerida,
        estatus_nombre: apiCase.estatus || 'Undefined',
      };
    }
  },
  created() {
    this.fetchFeaturedCases(); // Renamed method
  }
}
</script>

<style scoped>
.home-page { /* Renamed class */
  text-align: center;
}

.hero-header { /* Renamed class */
  background-color: #0056b3;
  color: white;
  padding: 3rem 1rem;
  margin-bottom: 2rem;
}

.hero-header h1 { /* Renamed class */
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.hero-header p { /* Renamed class */
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  opacity: 0.9;
}

.button-large { /* Renamed class (assuming .button and .button-primary are global) */
  padding: 0.8rem 2rem;
  font-size: 1.1rem;
}

.featured-cases-section, .how-it-works-section { /* Renamed classes */
  padding: 2rem 1rem;
  margin-bottom: 2rem;
}

.featured-cases-section h2, .how-it-works-section h2 { /* Renamed classes */
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.case-list { /* Renamed class */
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.loading-message, .error-message, .empty-message { /* Renamed classes */
  padding: 1rem;
  font-size: 1.1rem;
  color: #555;
}
.error-message { /* Renamed class */
  color: #dc3545;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  border-radius: 4px;
}

.how-it-works-steps { /* Renamed class */
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 1rem;
}

.step { /* Renamed class */
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
  width: 300px;
  text-align: center;
}

.step-icon { /* Renamed class */
  display: inline-block;
  background-color: #007bff;
  color: white;
  width: 40px;
  height: 40px;
  line-height: 40px;
  border-radius: 50%;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.step h3 { /* Renamed class */
  font-size: 1.3rem;
  color: #0056b3;
  margin-bottom: 0.5rem;
}
</style>
