<template>
  <div class="login-page"> <!-- Renamed class -->
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="handleLogin" class="common-form"> <!-- Renamed method, class -->
      <div class="form-group"> <!-- Renamed class -->
        <label for="id_morelia_or_email">ID Morelia o Correo Electrónico:</label> <!-- Anglicized for -->
        <input type="text" id="id_morelia_or_email" v-model="formData.id_morelia_o_email" required class="form-control">
      </div>
      <div class="form-group"> <!-- Renamed class -->
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="formData.password" required class="form-control">
      </div>

      <div v-if="apiError" class="error-message api-feedback-error"> <!-- Renamed data prop, class -->
        {{ apiError }}
      </div>
       <div v-if="successMessage" class="success-message api-feedback-success"> <!-- Renamed data prop, class -->
        {{ successMessage }}
      </div>

      <button type="submit" :disabled="loading" class="button button-primary"> <!-- Renamed data prop, class -->
        {{ loading ? 'Ingresando...' : 'Iniciar Sesión' }}
      </button>

      <p class="register-link"> <!-- Renamed class -->
        ¿No tienes cuenta? <router-link to="/register">Regístrate aquí</router-link> <!-- Updated path -->
      </p>
    </form>
  </div>
</template>

<script>
const API_BASE_URL = '/api/v1/crowdfunding';

export default {
  name: 'LoginPage', // Renamed component
  data() {
    return {
      formData: {
        id_morelia_o_email: '',
        password: '',
      },
      loading: false, // Renamed
      apiError: null, // Renamed
      successMessage: null, // Renamed
    };
  },
  methods: {
    async handleLogin() { // Renamed method
      this.loading = true;
      this.apiError = null;
      this.successMessage = null;

      try {
        const response = await fetch(`${API_BASE_URL}/usuarios/login/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.formData),
        });

        const responseData = await response.json();

        if (!response.ok) {
          this.apiError = responseData.error || `Error ${response.status}: ${response.statusText}`;
        } else {
          this.successMessage = `¡Bienvenido, ${responseData.usuario.first_name}!`;
          // Authentication state management (e.g., Vuex, Pinia) would go here.
          // localStorage.setItem('authToken', responseData.token);
          // this.$store.dispatch('auth/loginSuccess', responseData.usuario);

          alert("Login exitoso (simulado). Redirección no implementada.");
          // this.$router.push('/');
        }
      } catch (error) {
        console.error("Error during login:", error); // Anglicized log
        this.apiError = "Could not connect to the server or invalid response. Please try again later."; // Anglicized user message
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style scoped>
.login-page { /* Renamed class */
  max-width: 500px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.login-page h2 { /* Renamed class */
  text-align: center;
  color: #333;
  margin-bottom: 1.5rem;
}

.api-feedback-error, .api-feedback-success { /* Renamed classes */
  margin-bottom: 1rem;
  padding: 0.75rem;
  border-radius: 4px;
  text-align: center;
}
.api-feedback-error { /* Renamed class */
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}
.api-feedback-success { /* Renamed class */
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.button { /* Global style assumed */
  width: 100%;
  margin-top: 1rem;
}

.register-link { /* Renamed class */
  text-align: center;
  margin-top: 1.5rem;
  font-size: 0.9rem;
}
.register-link a { /* Renamed class */
  color: #007bff;
  text-decoration: none;
}
.register-link a:hover { /* Renamed class */
  text-decoration: underline;
}
</style>
