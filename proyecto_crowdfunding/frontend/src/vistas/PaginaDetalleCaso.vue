<template>
  <div class="pagina-detalle-caso" v-if="caso">
    <header class="detalle-caso-encabezado">
      <h1>{{ caso.titulo }}</h1>
      <p class="subtitulo-creador">
        Inciativa de: <strong>{{ caso.creador ? caso.creador.nombre_completo : 'Desconocido' }}</strong>
      </p>
      <div class="meta-info">
        <span>Categoría: {{ caso.categoria || 'No especificada' }}</span>
        <span>Estatus: {{ caso.estatus || 'No definido' }}</span>
        <span>Publicado: {{ formatearFecha(caso.fecha_publicacion) }}</span>
        <span>Finaliza: {{ formatearFecha(caso.fecha_fin) }}</span>
      </div>
    </header>

    <div class="detalle-caso-cuerpo">
      <div class="columna-principal">
        <img v-if="caso.imagen_promocional_url" :src="caso.imagen_promocional_url" :alt="'Imagen de ' + caso.titulo" class="imagen-principal-caso">

        <section class="seccion-descripcion">
          <h3>¿Quién Soy?</h3>
          <p>{{ caso.quien_soy }}</p>
          <h3>¿Qué Necesito?</h3>
          <p>{{ caso.que_necesito }}</p>
          <h3>¿Por Qué?</h3>
          <p>{{ caso.porque }}</p>
          <div v-if="caso.detalles_adicionales">
            <h3>Detalles Adicionales</h3>
            <p>{{ caso.detalles_adicionales }}</p>
          </div>
        </section>

        <section class="seccion-video" v-if="caso.video_promocional_url">
          <h3>Video Promocional</h3>
          <!-- Asumiendo que es una URL de YouTube o similar para embeber -->
          <!-- Para archivos de video directos, se usaría <video> tag -->
          <iframe width="560" height="315" :src="caso.video_promocional_url" frameborder="0" allowfullscreen></iframe>
        </section>

        <section class="seccion-articulos" v-if="caso.articulos && caso.articulos.length">
            <h3>Artículos/Necesidades Específicas</h3>
            <ul>
                <li v-for="articulo in caso.articulos" :key="articulo.id">
                    <strong>{{ articulo.descripcion }}</strong> - {{ formatearMoneda(articulo.precio) }} (Recibo: {{ articulo.recibo_tipo }})
                </li>
            </ul>
        </section>

      </div>

      <aside class="columna-lateral">
        <div class="panel-fondeo">
          <h3>Apoya este Caso</h3>
          <div class="progreso-fondeo">
            <div class="barra-progreso-detalle" :style="{ width: porcentajeObtenido + '%' }">
              {{ porcentajeObtenido.toFixed(0) }}%
            </div>
          </div>
          <p class="montos">
            <strong>{{ formatearMoneda(caso.cantidad_obtenida) }}</strong> recaudado de
            <span>{{ formatearMoneda(caso.cantidad_requerida) }}</span>
          </p>
          <!-- Placeholder para botones de fondeo/interacción -->
          <button class="boton boton-primario boton-grande btn-apoyar">Quiero Apoyar</button>
          <button class="boton boton-secundario btn-compartir">Compartir</button>
        </div>
        <div class="panel-creador" v-if="caso.creador">
          <h4>Sobre el Creador</h4>
          <p><strong>{{ caso.creador.nombre_completo }}</strong></p>
          <p>ID Morelia: {{ caso.creador.id_morelia }}</p>
          <p>Email: {{ caso.creador.email }}</p> <!-- Considerar privacidad -->
          <!-- Más info del creador si es relevante -->
        </div>
      </aside>
    </div>

    <!-- Placeholder para secciones de preguntas, actualizaciones, etc. -->
    <section class="seccion-interaccion">
        <h3>Preguntas y Respuestas</h3>
        <p>(Próximamente)</p>
        <h3>Actualizaciones del Proyecto</h3>
        <p>(Próximamente)</p>
    </section>

  </div>
  <div v-if="cargando" class="mensaje-carga">Cargando detalles del caso...</div>
  <div v-if="error" class="mensaje-error">Error al cargar el caso: {{ error }}</div>
</template>

<script>
const API_BASE_URL = '/api/v1/crowdfunding';
const MEDIA_URL_BASE = '/media/'; // Debería ser global/configurable

export default {
  name: 'PaginaDetalleCaso',
  props: ['casoId'], // Recibido de la ruta (ej. /casos/:casoId)
  data() {
    return {
      caso: null,
      cargando: false,
      error: null,
    };
  },
  computed: {
    porcentajeObtenido() {
      if (!this.caso || !this.caso.cantidad_requerida || this.caso.cantidad_requerida === 0) {
        return 0;
      }
      const porcentaje = (this.caso.cantidad_obtenida / this.caso.cantidad_requerida) * 100;
      return Math.min(porcentaje, 100);
    }
  },
  methods: {
    async fetchDetalleCaso() {
      this.cargando = true;
      this.error = null;
      try {
        const response = await fetch(`${API_BASE_URL}/casos/${this.casoId}/`);
        if (!response.ok) {
          if (response.status === 404) {
            throw new Error('Caso no encontrado.');
          }
          throw new Error(`Error del servidor: ${response.status} ${response.statusText}`);
        }
        const apiCaso = await response.json();
        this.caso = this.mapApiDataToLocal(apiCaso);

      } catch (error) {
        console.error(`Error fetching detalle del caso ${this.casoId}:`, error);
        this.error = error.message;
      } finally {
        this.cargando = false;
      }
    },
    mapApiDataToLocal(apiCaso) {
      // Mapear y procesar datos de la API para el componente
      let imagenUrl = '';
      if (apiCaso.imagen_promocional) {
        imagenUrl = `${MEDIA_URL_BASE}${apiCaso.imagen_promocional}`;
      }
      // Asumimos que video_promocional es una URL completa o un ID de video para un iframe
      // Si es un path relativo a MEDIA_ROOT, se construiría igual que imagenUrl.
      // Por ahora, si es una URL de YouTube, debería funcionar directamente.
      // Si es un path de archivo, se necesitaría una lógica para construir la URL completa.

      return {
        ...apiCaso, // Copia todos los campos
        imagen_promocional_url: imagenUrl,
        // Si video_promocional es un path y no una URL completa:
        // video_promocional_url: apiCaso.video_promocional ? `${MEDIA_URL_BASE}${apiCaso.video_promocional}` : null,
        // Si ya es una URL (ej. YouTube), simplemente usarla:
        video_promocional_url: apiCaso.video_promocional,
        // El backend ya envía 'creador' como un objeto anidado y 'articulos' como lista.
        // Solo necesitamos asegurarnos que los nombres de campo coincidan o mapearlos aquí.
        // El backend envía: categoria (nombre), estatus (nombre)
        categoria: apiCaso.categoria, // Ya es el nombre
        estatus: apiCaso.estatus, // Ya es el nombre
      };
    },
    formatearMoneda(valor) {
      if (typeof valor !== 'number') {
        valor = parseFloat(valor) || 0;
      }
      return `$${valor.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}`;
    },
    formatearFecha(fechaIso) {
      if (!fechaIso) return 'N/A';
      try {
        const fecha = new Date(fechaIso);
        return fecha.toLocaleDateString('es-MX', { year: 'numeric', month: 'long', day: 'numeric' });
      } catch (e) {
        return fechaIso; // Devolver original si hay error
      }
    }
  },
  created() {
    if (this.casoId) {
      this.fetchDetalleCaso();
    } else {
      this.error = "No se especificó un ID de caso.";
    }
  },
  // Podríamos usar watch para recargar si casoId cambia dinámicamente (menos común para rutas de página)
  // watch: {
  //   casoId(newId) {
  //     if (newId) this.fetchDetalleCaso();
  //   }
  // }
}
</script>

<style scoped>
.pagina-detalle-caso {
  max-width: 1000px; /* Un poco más ancho para detalles */
  margin: 1rem auto;
  padding: 1rem;
}

.detalle-caso-encabezado {
  background-color: #e9ecef;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
  text-align: left;
}
.detalle-caso-encabezado h1 {
  font-size: 2.3rem;
  color: #2c3e50;
  margin-top: 0;
  margin-bottom: 0.5rem;
}
.subtitulo-creador {
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

.detalle-caso-cuerpo {
  display: flex;
  flex-wrap: wrap; /* Para responsividad */
  gap: 2rem;
}

.columna-principal {
  flex: 3; /* Toma más espacio */
  min-width: 300px; /* Para que no se encoja demasiado */
}

.imagen-principal-caso {
  width: 100%;
  max-height: 450px;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  background-color: #f0f0f0;
}

.seccion-descripcion h3, .seccion-video h3, .seccion-articulos h3, .seccion-interaccion h3 {
  font-size: 1.5rem;
  color: #0056b3;
  margin-top: 2rem;
  margin-bottom: 0.75rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #007bff;
}
.seccion-descripcion p {
  line-height: 1.7;
  margin-bottom: 1rem;
}
.seccion-articulos ul {
    list-style: disc;
    padding-left: 20px;
}
.seccion-articulos li {
    margin-bottom: 0.5rem;
}


.seccion-video iframe {
    max-width: 100%;
    border-radius: 8px;
}

.columna-lateral {
  flex: 1;
  min-width: 280px; /* Para que no se encoja demasiado */
}

.panel-fondeo, .panel-creador {
  background-color: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}
.panel-fondeo h3, .panel-creador h4 {
  margin-top: 0;
  color: #343a40;
}
.progreso-fondeo {
  background-color: #e0e0e0;
  border-radius: 20px; /* Más redondeado */
  height: 25px; /* Más alto */
  margin-bottom: 0.75rem;
  overflow: hidden;
  position: relative;
}
.barra-progreso-detalle {
  background-color: #28a745; /* Verde más vibrante */
  height: 100%;
  transition: width 0.5s ease;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 0.9rem;
}
.montos {
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}
.montos strong {
  color: #28a745;
  font-size: 1.5rem;
}
.montos span {
    font-size: 1rem;
    color: #6c757d;
}
.btn-apoyar {
  width: 100%;
  margin-bottom: 0.75rem;
}
.btn-compartir {
  width: 100%;
}

.panel-creador p {
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
}

.seccion-interaccion {
    margin-top: 3rem;
    padding: 1.5rem;
    background-color: #fff;
    border-radius: 8px;
}

.mensaje-carga, .mensaje-error {
  padding: 1rem;
  text-align: center;
}
</style>
