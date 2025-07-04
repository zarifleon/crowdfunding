<template>
  <div class="tarjeta-caso">
    <img v-if="caso.imagen_promocional_url" :src="caso.imagen_promocional_url" :alt="'Imagen de ' + caso.titulo" class="tarjeta-caso-imagen">
    <div class="tarjeta-caso-contenido">
      <h3>{{ caso.titulo }}</h3>
      <p class="creador">Por: {{ caso.creador_nombre_completo || caso.creador_id }}</p>
      <p class="descripcion-corta">{{ truncarTexto(caso.quien_soy, 100) }}</p>
      <div class="progreso">
        <div class="barra-progreso" :style="{ width: porcentajeObtenido + '%' }"></div>
      </div>
      <p>{{ formatearMoneda(caso.cantidad_obtenida) }} de {{ formatearMoneda(caso.cantidad_requerida) }}</p>
      <p>Estatus: {{ caso.estatus_nombre || 'No definido' }}</p>
      <router-link v-if="caso.id" :to="{ name: 'DetalleCaso', params: { casoId: caso.id } }" class="boton-detalle">
        Ver Detalles
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TarjetaCaso',
  props: {
    caso: {
      type: Object,
      required: true,
      default: () => ({ // Valores por defecto para prevenir errores si `caso` no está completamente formado
        id: null,
        titulo: 'Caso Desconocido',
        creador_nombre_completo: 'N/A',
        creador_id: 'N/A',
        quien_soy: 'Sin descripción.',
        imagen_promocional_url: '', // Asumimos que la URL completa vendrá del backend o se construirá
        cantidad_obtenida: 0,
        cantidad_requerida: 0,
        estatus_nombre: 'Indefinido',
      })
    }
  },
  computed: {
    porcentajeObtenido() {
      if (!this.caso.cantidad_requerida || this.caso.cantidad_requerida === 0) {
        return 0;
      }
      const porcentaje = (this.caso.cantidad_obtenida / this.caso.cantidad_requerida) * 100;
      return Math.min(porcentaje, 100); // No exceder el 100%
    }
  },
  methods: {
    truncarTexto(texto, longitudMaxima) {
      if (!texto) return '';
      if (texto.length <= longitudMaxima) {
        return texto;
      }
      return texto.substring(0, longitudMaxima) + '...';
    },
    formatearMoneda(valor) {
      if (typeof valor !== 'number') {
        valor = parseFloat(valor) || 0;
      }
      // Formato simple, se puede mejorar con Intl.NumberFormat si es necesario
      return `$${valor.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}`;
    }
  }
}
</script>

<style scoped>
.tarjeta-caso {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin: 1rem;
  width: 300px; /* Ancho fijo para ejemplo */
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
}

.tarjeta-caso-imagen {
  width: 100%;
  height: 180px;
  object-fit: cover;
  background-color: #f0f0f0; /* Placeholder si no hay imagen */
}

.tarjeta-caso-contenido {
  padding: 1rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.tarjeta-caso-contenido h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
}

.creador {
  font-size: 0.9rem;
  color: #555;
  margin-bottom: 0.75rem;
}

.descripcion-corta {
  font-size: 0.9rem;
  color: #333;
  flex-grow: 1; /* Empuja el progreso y botón hacia abajo */
  margin-bottom: 1rem;
}

.progreso {
  background-color: #e0e0e0;
  border-radius: 4px;
  height: 10px;
  margin-bottom: 0.5rem;
  overflow: hidden; /* Para que la barra interior no se salga */
}

.barra-progreso {
  background-color: #4caf50; /* Color verde para el progreso */
  height: 100%;
  transition: width 0.3s ease;
}

.tarjeta-caso-contenido p {
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.boton-detalle {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  text-align: center;
  border-radius: 4px;
  text-decoration: none;
  margin-top: auto; /* Empuja el botón al final de la tarjeta */
}

.boton-detalle:hover {
  background-color: #0056b3;
}
</style>
