<template>
  <div class="case-card"> <!-- Renamed class -->
    <img v-if="caseItem.imagen_promocional_url" :src="caseItem.imagen_promocional_url" :alt="'Image of ' + caseItem.titulo" class="case-card-image"> <!-- Renamed class, prop -->
    <div class="case-card-content"> <!-- Renamed class -->
      <h3>{{ caseItem.titulo }}</h3> <!-- Renamed prop -->
      <p class="creator">By: {{ caseItem.creador_nombre_completo || caseItem.creador_id }}</p> <!-- Renamed class, prop -->
      <p class="short-description">{{ truncateText(caseItem.quien_soy, 100) }}</p> <!-- Renamed class, prop -->
      <div class="progress-bar-container"> <!-- Renamed class -->
        <div class="progress-bar" :style="{ width: percentageFunded + '%' }"></div> <!-- Renamed class, computed prop -->
      </div>
      <p>{{ formatCurrency(caseItem.cantidad_obtenida) }} of {{ formatCurrency(caseItem.cantidad_requerida) }}</p> <!-- Renamed method, prop -->
      <p>Status: {{ caseItem.estatus_nombre || 'Not defined' }}</p> <!-- Renamed prop -->
      <router-link v-if="caseItem.id" :to="{ name: 'CaseDetail', params: { caseId: caseItem.id } }" class="detail-button"> <!-- Renamed prop, route name -->
        View Details
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CaseCard', // Renamed component
  props: {
    caseItem: { // Renamed prop from 'caso' to 'caseItem' for clarity in English context
      type: Object,
      required: true,
      default: () => ({
        id: null,
        titulo: 'Unknown Case',
        creador_nombre_completo: 'N/A',
        creador_id: 'N/A',
        quien_soy: 'No description.',
        imagen_promocional_url: '',
        cantidad_obtenida: 0,
        cantidad_requerida: 0,
        estatus_nombre: 'Undefined',
      })
    }
  },
  computed: {
    percentageFunded() { // Renamed computed property
      if (!this.caseItem.cantidad_requerida || this.caseItem.cantidad_requerida === 0) {
        return 0;
      }
      const percentage = (this.caseItem.cantidad_obtenida / this.caseItem.cantidad_requerida) * 100;
      return Math.min(percentage, 100);
    }
  },
  methods: {
    truncateText(text, maxLength) { // Renamed method
      if (!text) return '';
      if (text.length <= maxLength) {
        return text;
      }
      return text.substring(0, maxLength) + '...';
    },
    formatCurrency(value) { // Renamed method
      if (typeof value !== 'number') {
        value = parseFloat(value) || 0;
      }
      return `$${value.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}`;
    }
  }
}
</script>

<style scoped>
.case-card { /* Renamed class */
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin: 1rem;
  width: 300px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
}

.case-card-image { /* Renamed class */
  width: 100%;
  height: 180px;
  object-fit: cover;
  background-color: #f0f0f0;
}

.case-card-content { /* Renamed class */
  padding: 1rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.case-card-content h3 { /* Renamed class */
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.25rem;
}

.creator { /* Renamed class */
  font-size: 0.9rem;
  color: #555;
  margin-bottom: 0.75rem;
}

.short-description { /* Renamed class */
  font-size: 0.9rem;
  color: #333;
  flex-grow: 1;
  margin-bottom: 1rem;
}

.progress-bar-container { /* Renamed class */
  background-color: #e0e0e0;
  border-radius: 4px;
  height: 10px;
  margin-bottom: 0.5rem;
  overflow: hidden;
}

.progress-bar { /* Renamed class */
  background-color: #4caf50;
  height: 100%;
  transition: width 0.3s ease;
}

.case-card-content p { /* Renamed class */
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.detail-button { /* Renamed class */
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  text-align: center;
  border-radius: 4px;
  text-decoration: none;
  margin-top: auto;
}

.detail-button:hover { /* Renamed class */
  background-color: #0056b3;
}
</style>
