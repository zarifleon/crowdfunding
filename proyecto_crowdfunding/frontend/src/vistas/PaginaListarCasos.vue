<template>
  <div class="pagina-listar-casos">
    <header class="encabezado-pagina">
      <h1>Explora Todos los Casos</h1>
      <p>Encuentra proyectos que te inspiren y apóyalos.</p>
    </header>

    <div v-if="cargando" class="mensaje-carga">
      Cargando casos...
    </div>
    <div v-if="error" class="mensaje-error">
      Error al cargar los casos: {{ error }}
    </div>

    <div class="filtros-y-orden" v-if="!cargando && !error && casos.length">
      <!-- Placeholder para futuros filtros y opciones de ordenación -->
      <p>Filtros y ordenación (próximamente)</p>
    </div>

    <div class="grilla-casos" v-if="!cargando && !error && casos.length">
      <TarjetaCaso v-for="caso in casos" :key="caso.id" :caso="mapCasoData(caso)" />
    </div>

    <div v-if="!cargando && !error && !casos.length" class="mensaje-vacio">
      Actualmente no hay casos publicados. ¡Intenta de nuevo más tarde!
    </div>

    <!-- Placeholder para paginación -->
    <div class="paginacion" v-if="!cargando && !error && casos.length > 10">
        <p>Paginación (próximamente)</p>
    </div>
  </div>
</template>

<script>
import TarjetaCaso from '../componentes/TarjetaCaso.vue';
const API_BASE_URL = '/api/v1/crowdfunding';

export default {
  name: 'PaginaListarCasos',
  components: {
    TarjetaCaso
  },
  data() {
    return {
      casos: [],
      cargando: false,
      error: null,
      // Opciones de paginación podrían ir aquí: currentPage, totalPages, etc.
    };
  },
  methods: {
    async fetchTodosLosCasos() {
      this.cargando = true;
      this.error = null;
      try {
        const response = await fetch(`${API_BASE_URL}/casos/`);
        if (!response.ok) {
          throw new Error(`Error del servidor: ${response.status} ${response.statusText}`);
        }
        this.casos = await response.json();
      } catch (error) {
        console.error("Error fetching todos los casos:", error);
        this.error = error.message;
      } finally {
        this.cargando = false;
      }
    },
    mapCasoData(apiCaso) {
      // Similar al de PaginaInicio.vue, idealmente esto sería un helper global o parte de un servicio.
      let imagenUrl = '';
      if (apiCaso.imagen_promocional) {
        const mediaUrlBase = '/media/';
        imagenUrl = `${mediaUrlBase}${apiCaso.imagen_promocional}`;
      }

      return {
        id: apiCaso.id,
        titulo: apiCaso.titulo,
        creador_nombre_completo: apiCaso.creador ? apiCaso.creador.nombre_completo : (apiCaso.creador_id || 'N/A'),
        creador_id: apiCaso.creador ? apiCaso.creador.id_morelia : (apiCaso.creador_id || 'N/A'),
        quien_soy: apiCaso.quien_soy,
        imagen_promocional_url: imagenUrl,
        cantidad_obtenida: apiCaso.cantidad_obtenida,
        cantidad_requerida: apiCaso.cantidad_requerida,
        estatus_nombre: apiCaso.estatus || 'Indefinido',
      };
    }
  },
  created() {
    this.fetchTodosLosCasos();
  }
}
</script>

<style scoped>
.pagina-listar-casos {
  padding: 1rem;
}

.encabezado-pagina {
  background-color: #f8f9fa; /* Color de fondo suave */
  padding: 2rem 1rem;
  margin-bottom: 2rem;
  border-radius: 8px;
  text-align: center;
}

.encabezado-pagina h1 {
  font-size: 2.2rem;
  color: #343a40;
  margin-bottom: 0.5rem;
}

.encabezado-pagina p {
  font-size: 1.1rem;
  color: #6c757d;
}

.filtros-y-orden {
  margin-bottom: 1.5rem;
  padding: 1rem;
  background-color: #fff;
  border-radius: 6px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  text-align: center; /* Placeholder */
}

.grilla-casos {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); /* Diseño de grilla responsiva */
  gap: 1.5rem; /* Espacio entre tarjetas */
}

.mensaje-carga, .mensaje-error, .mensaje-vacio {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
  color: #555;
}
.mensaje-error {
  color: #dc3545;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  border-radius: 4px;
}
.mensaje-vacio {
  background-color: #e9ecef;
  border-radius: 4px;
}

.paginacion {
  margin-top: 2rem;
  text-align: center;
  padding: 1rem;
  background-color: #fff;
  border-radius: 6px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
</style>
