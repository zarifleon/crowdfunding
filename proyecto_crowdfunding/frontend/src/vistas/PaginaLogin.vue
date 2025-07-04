<template>
  <div class="pagina-login">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="manejarLogin" class="formulario-comun">
      <div class="form-grupo">
        <label for="id_morelia_o_email">ID Morelia o Correo Electrónico:</label>
        <input type="text" id="id_morelia_o_email" v-model="formData.id_morelia_o_email" required class="form-control">
      </div>
      <div class="form-grupo">
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="formData.password" required class="form-control">
      </div>

      <div v-if="errorApi" class="mensaje-error api-error">
        {{ errorApi }}
      </div>
       <div v-if="mensajeExito" class="mensaje-exito api-exito">
        {{ mensajeExito }} <!-- Aunque usualmente se redirige en login exitoso -->
      </div>

      <button type="submit" :disabled="cargando" class="boton boton-primario">
        {{ cargando ? 'Ingresando...' : 'Iniciar Sesión' }}
      </button>

      <p class="enlace-registro">
        ¿No tienes cuenta? <router-link to="/registrar">Regístrate aquí</router-link>
      </p>
    </form>
  </div>
</template>

<script>
const API_BASE_URL = '/api/v1/crowdfunding';
// En una app real, el manejo del estado de autenticación (ej. guardar token, datos de usuario)
// se haría a través de Vuex, Pinia o un servicio de autenticación dedicado.

export default {
  name: 'PaginaLogin',
  data() {
    return {
      formData: {
        id_morelia_o_email: '',
        password: '',
      },
      cargando: false,
      errorApi: null,
      mensajeExito: null, // Generalmente no se usa en login, se redirige
    };
  },
  methods: {
    async manejarLogin() {
      this.cargando = true;
      this.errorApi = null;
      this.mensajeExito = null;

      try {
        const response = await fetch(`${API_BASE_URL}/usuarios/login/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            // CSRF token si es necesario
          },
          body: JSON.stringify(this.formData),
        });

        const responseData = await response.json();

        if (!response.ok) {
          this.errorApi = responseData.error || `Error ${response.status}: ${response.statusText}`;
        } else {
          this.mensajeExito = `¡Bienvenido, ${responseData.usuario.first_name}!`;
          // Aquí se manejaría el estado de autenticación global:
          // 1. Guardar el token de acceso (si la API devuelve uno, ej. JWT).
          // 2. Guardar los datos del usuario en el store (Vuex/Pinia).
          // 3. Actualizar el estado `usuarioAutenticado` en el store.
          // Ejemplo:
          // localStorage.setItem('authToken', responseData.token); // Si hay token
          // this.$store.dispatch('auth/loginExitoso', responseData.usuario);

          alert("Login exitoso (simulado). Redirección no implementada.");
          // Idealmente, redirigir:
          // this.$router.push('/'); // O a la página de perfil/dashboard
        }
      } catch (error) {
        console.error("Error en el inicio de sesión:", error);
        this.errorApi = "No se pudo conectar con el servidor o respuesta inválida. Intenta de nuevo más tarde.";
      } finally {
        this.cargando = false;
      }
    }
  }
}
</script>

<style scoped>
.pagina-login {
  max-width: 500px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.pagina-login h2 {
  text-align: center;
  color: #333;
  margin-bottom: 1.5rem;
}

.api-error, .api-exito {
  margin-bottom: 1rem;
  padding: 0.75rem;
  border-radius: 4px;
  text-align: center;
}
.api-error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}
.api-exito { /* Menos común ver esto en login, usualmente se redirige */
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.boton {
  width: 100%;
  margin-top: 1rem;
}

.enlace-registro {
  text-align: center;
  margin-top: 1.5rem;
  font-size: 0.9rem;
}
.enlace-registro a {
  color: #007bff;
  text-decoration: none;
}
.enlace-registro a:hover {
  text-decoration: underline;
}
</style>
