<template>
  <div class="pagina-inicio">
    <header class="encabezado-hero">
      <h1>Encuentra y Apoya Proyectos Locales</h1>
      <p>Tu contribución puede hacer la diferencia en Morelia.</p>
      <router-link to="/casos" class="boton boton-primario boton-grande">Explorar Casos</router-link>
    </header>

    <section class="seccion-casos-destacados">
      <h2>Casos Destacados</h2>
      <div v-if="cargandoCasos" class="mensaje-carga">
        Cargando casos...
      </div>
      <div v-if="errorCasos" class="mensaje-error">
        Error al cargar los casos: {{ errorCasos }}
      </div>
      <div class="lista-casos" v-if="!cargandoCasos && !errorCasos && casosDestacados.length">
        <TarjetaCaso v-for="caso in casosDestacados" :key="caso.id" :caso="mapCasoData(caso)" />
      </div>
      <div v-if="!cargandoCasos && !errorCasos && !casosDestacados.length" class="mensaje-vacio">
        No hay casos destacados en este momento. ¡Vuelve pronto!
      </div>
    </section>

    <section class="seccion-como-funciona">
      <h2>¿Cómo Funciona?</h2>
      <div class="pasos-como-funciona">
        <div class="paso">
          <span class="icono-paso">1</span>
          <h3>Registra tu Idea</h3>
          <p>Presenta tu proyecto o necesidad a la comunidad.</p>
        </div>
        <div class="paso">
          <span class="icono-paso">2</span>
          <h3>Recibe Apoyo</h3>
          <p>Ciudadanos y empresas pueden aportar a tu causa.</p>
        </div>
        <div class="paso">
          <span class="icono-paso">3</span>
          <h3>Hazlo Realidad</h3>
          <p>Utiliza los fondos para concretar tu proyecto y muestra tus avances.</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import TarjetaCaso from '../componentes/TarjetaCaso.vue';
// En una app real, la URL base de la API vendría de una configuración.
const API_BASE_URL = '/api/v1/crowdfunding'; // Asumiendo que el proxy de desarrollo o Nginx manejan esto.

export default {
  name: 'PaginaInicio',
  components: {
    TarjetaCaso
  },
  data() {
    return {
      casosDestacados: [],
      cargandoCasos: false,
      errorCasos: null,
    };
  },
  methods: {
    async fetchCasosDestacados() {
      this.cargandoCasos = true;
      this.errorCasos = null;
      try {
        // Simulación: En una API real, podría haber un endpoint para casos destacados
        // o podríamos tomar los primeros N de la lista general.
        const response = await fetch(`${API_BASE_URL}/casos/`); // Usamos el endpoint de listar todos
        if (!response.ok) {
          throw new Error(`Error del servidor: ${response.status} ${response.statusText}`);
        }
        const todosLosCasos = await response.json();
        // Simplemente tomamos los primeros 3 como "destacados" para este ejemplo.
        this.casosDestacados = todosLosCasos.slice(0, 3);
      } catch (error) {
        console.error("Error fetching casos destacados:", error);
        this.errorCasos = error.message;
      } finally {
        this.cargandoCasos = false;
      }
    },
    mapCasoData(apiCaso) {
      // Mapea los datos de la API al formato esperado por TarjetaCaso si es necesario.
      // Especialmente para la imagen_promocional_url.
      let imagenUrl = '';
      if (apiCaso.imagen_promocional) {
        // Asumimos que apiCaso.imagen_promocional es una ruta relativa desde MEDIA_URL
        // En un entorno real, MEDIA_URL debería estar disponible globalmente (e.g., Vue.prototype.$mediaUrl o similar)
        const mediaUrlBase = '/media/'; // Hardcodeado por ahora, debería ser configurable
        imagenUrl = `${mediaUrlBase}${apiCaso.imagen_promocional}`;
      }

      return {
        id: apiCaso.id,
        titulo: apiCaso.titulo,
        creador_nombre_completo: apiCaso.creador ? apiCaso.creador.nombre_completo : 'N/A', // Asumiendo que el backend envía esto
        creador_id: apiCaso.creador ? apiCaso.creador.id_morelia : 'N/A',
        quien_soy: apiCaso.quien_soy, // O cualquier otro campo para descripción corta
        imagen_promocional_url: imagenUrl,
        cantidad_obtenida: apiCaso.cantidad_obtenida,
        cantidad_requerida: apiCaso.cantidad_requerida,
        estatus_nombre: apiCaso.estatus || 'Indefinido', // Asumiendo que el backend envía el nombre del estatus
      };
    }
  },
  created() {
    this.fetchCasosDestacados();
  }
}
</script>

<style scoped>
.pagina-inicio {
  text-align: center;
}

.encabezado-hero {
  background-color: #0056b3; /* Un azul más oscuro para el hero */
  color: white;
  padding: 3rem 1rem;
  margin-bottom: 2rem;
}

.encabezado-hero h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.encabezado-hero p {
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
  opacity: 0.9;
}

.boton-grande {
  padding: 0.8rem 2rem;
  font-size: 1.1rem;
}

.seccion-casos-destacados, .seccion-como-funciona {
  padding: 2rem 1rem;
  margin-bottom: 2rem;
}

.seccion-casos-destacados h2, .seccion-como-funciona h2 {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: #333;
}

.lista-casos {
  display: flex;
  flex-wrap: wrap; /* Permitir que las tarjetas pasen a la siguiente línea */
  justify-content: center; /* Centrar las tarjetas */
  gap: 1rem; /* Espacio entre tarjetas */
}

.mensaje-carga, .mensaje-error, .mensaje-vacio {
  padding: 1rem;
  font-size: 1.1rem;
  color: #555;
}
.mensaje-error {
  color: #dc3545;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  border-radius: 4px;
}

.pasos-como-funciona {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 1rem;
}

.paso {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
  width: 300px;
  text-align: center;
}

.icono-paso {
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

.paso h3 {
  font-size: 1.3rem;
  color: #0056b3;
  margin-bottom: 0.5rem;
}
</style>
