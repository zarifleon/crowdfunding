<template>
  <nav class="barra-navegacion">
    <div class="nav-marca">
      <router-link to="/">CrowdMorelia</router-link>
    </div>
    <ul class="nav-enlaces">
      <li>
        <router-link to="/">Inicio</router-link>
      </li>
      <!-- Estos enlaces podrían cambiar si el usuario está autenticado -->
      <li v-if="!usuarioAutenticado">
        <router-link to="/registrar">Registrar</router-link>
      </li>
      <li v-if="!usuarioAutenticado">
        <router-link to="/login">Iniciar Sesión</router-link>
      </li>
      <li v-if="usuarioAutenticado">
        <router-link to="/crear-caso">Crear Caso</router-link>
      </li>
      <li v-if="usuarioAutenticado">
        <router-link to="/perfil">Mi Perfil</router-link> <!-- Asumiendo una ruta de perfil -->
      </li>
      <li v_if="usuarioAutenticado">
        <button @click="manejarLogout" class="boton-logout">Cerrar Sesión</button>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'BarraNavegacion',
  // En una aplicación real, el estado de autenticación vendría de Vuex o un servicio de autenticación.
  // Por ahora, es un placeholder.
  data() {
    return {
      // Este estado debería ser global (ej. Vuex store)
      // usuarioAutenticado: false
    };
  },
  computed: {
    // Ejemplo si se usara Vuex:
    // ...mapState('auth', ['usuarioAutenticado'])
    // O un prop/evento si se maneja localmente de forma simple:
    usuarioAutenticado() {
      // Placeholder: En una app real, esto se determinaría por el estado de autenticación global.
      // Podría ser un simple check de un token en localStorage o una variable en un store.
      // Por ejemplo, si tuviéramos un store simple:
      // return this.$store.state.autenticado;
      return false; // Cambiar a true para ver enlaces de usuario autenticado
    }
  },
  methods: {
    manejarLogout() {
      console.log("Manejador de Logout llamado");
      // Aquí iría la lógica para:
      // 1. Limpiar el token/sesión del usuario.
      // 2. Actualizar el estado global de autenticación (ej. en Vuex).
      // 3. Redirigir al usuario a la página de inicio o login.
      // this.$store.dispatch('auth/logout'); // Ejemplo con Vuex
      // this.$router.push('/login');
      alert("Funcionalidad de Cerrar Sesión no implementada completamente.");
    }
    // Se podrían añadir métodos para login/registro si se manejan con modales desde aquí.
  }
}
</script>

<style scoped>
.barra-navegacion {
  background-color: #343a40; /* Bootstrap dark-like color */
  padding: 0.75rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
}

.nav-marca a {
  color: white;
  text-decoration: none;
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-enlaces {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  align-items: center;
}

.nav-enlaces li {
  margin-left: 1.5rem;
}

.nav-enlaces a {
  color: #adb5bd; /* Light gray for links */
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.2s ease-in-out;
}

.nav-enlaces a:hover,
.nav-enlaces a.router-link-exact-active { /* Estilo para el enlace activo */
  color: white;
}

.boton-logout {
  background-color: transparent;
  color: #adb5bd;
  border: 1px solid #adb5bd;
  padding: 0.375rem 0.75rem;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 1rem;
  transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out;
}

.boton-logout:hover {
  color: white;
  background-color: #495057;
}
</style>
