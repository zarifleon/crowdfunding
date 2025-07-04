<template>
  <div id="app-container">
    <NavigationBar /> <!-- Updated component name -->
    <main class="main-content"> <!-- Renamed class -->
      <router-view />
    </main>
    <footer class="page-footer"> <!-- Renamed class -->
      <p>&copy; 2024 Ayuntamiento de Morelia - Crowdfunding Morelia</p>
    </footer>
  </div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue'; // Updated import path and component name

export default {
  name: 'App',
  components: {
    NavigationBar // Updated component name
  }
}
</script>

<style>
/* Estilos Globales (pueden ir en un archivo CSS separado e importarse en main.js) */
body {
  margin: 0;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  line-height: 1.6;
  background-color: #f4f7f6;
  color: #333;
}

#app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.contenido-principal {
  flex: 1;
  padding: 1rem; /* Espaciado alrededor del contenido principal */
  max-width: 1200px; /* Ancho máximo para el contenido */
  margin: 0 auto; /* Centrar el contenido */
  width: 100%;
}

.pie-pagina {
  text-align: center;
  padding: 1rem;
  background-color: #343a40; /* Similar a la barra de navegación */
  color: white;
  font-size: 0.9rem;
}

/* Estilos generales para botones para consistencia */
.boton {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
  text-decoration: none;
  border: none;
  transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
}

.boton-primario {
  background-color: #007bff;
  color: white;
}
.boton-primario:hover {
  background-color: #0056b3;
}

.boton-secundario {
  background-color: #6c757d;
  color: white;
}
.boton-secundario:hover {
  background-color: #545b62;
}

/* Estilos para formularios (ejemplo) */
.form-grupo {
  margin-bottom: 1rem;
}

.form-grupo label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.form-control {
  width: 100%;
  padding: 0.75rem;
  font-size: 1rem;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  box-sizing: border-box; /* Para que padding no afecte el ancho total */
}

.form-control:focus {
  border-color: #80bdff;
  outline: 0;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.error-mensaje {
  color: #dc3545; /* Rojo para errores */
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

</style>
