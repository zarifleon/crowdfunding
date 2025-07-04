<template>
  <div class="register-page"> <!-- Renamed class -->
    <h2>Registro de Nuevo Usuario</h2>
    <form @submit.prevent="handleRegistration" class="common-form"> <!-- Renamed method, class -->
      <div class="form-group"> <!-- Renamed class -->
        <label for="id_morelia">ID Morelia (CURP o Identificador Único):</label>
        <input type="text" id="id_morelia" v-model="formData.id_morelia" required class="form-control">
      </div>
      <div class="form-group"> <!-- Renamed class -->
        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" v-model="formData.email" required class="form-control">
      </div>
      <div class="form-group"> <!-- Renamed class -->
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="formData.password" required class="form-control">
      </div>
      <div class="form-group"> <!-- Renamed class -->
        <label for="confirm_password">Confirmar Contraseña:</label> <!-- Renamed id/for -->
        <input type="password" id="confirm_password" v-model="formData.confirm_password" required class="form-control">
      </div>
      <div class="form-group"> <!-- Renamed class -->
        <label for="first_name">Nombres:</label>
        <input type="text" id="first_name" v-model="formData.first_name" required class="form-control">
      </div>
      <div class="form-group"> <!-- Renamed class -->
        <label for="last_name">Apellidos:</label>
        <input type="text" id="last_name" v.model="formData.last_name" required class="form-control">
      </div>

      <div v-if="apiError" class="error-message api-feedback-error"> <!-- Renamed data prop, class -->
        {{ apiError }}
      </div>
      <div v-if="successMessage" class="success-message api-feedback-success"> <!-- Renamed data prop, class -->
        {{ successMessage }}
      </div>

      <button type="submit" :disabled="loading" class="button button-primary"> <!-- Renamed data prop, class -->
        {{ loading ? 'Registrando...' : 'Registrar Usuario' }}
      </button>
    </form>
  </div>
</template>

<script>
const API_BASE_URL = '/api/v1/crowdfunding';

export default {
  name: 'RegisterPage', // Renamed component
  data() {
    return {
      formData: {
        id_morelia: '',
        email: '',
        password: '',
        confirm_password: '', // Corrected from confirmar_password for consistency
        first_name: '',
        last_name: '',
      },
      loading: false, // Renamed
      apiError: null, // Renamed
      successMessage: null, // Renamed
    };
  },
  methods: {
    async handleRegistration() { // Renamed method
      this.loading = true;
      this.apiError = null;
      this.successMessage = null;

      if (this.formData.password !== this.formData.confirm_password) {
        this.apiError = "Las contraseñas no coinciden.";
        this.loading = false;
        return;
      }

      const payload = { ...this.formData };
      delete payload.confirm_password;

      try {
        const response = await fetch(`${API_BASE_URL}/usuarios/registrar/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(payload),
        });

        const responseData = await response.json();

        if (!response.ok) {
          this.apiError = responseData.error || `Error ${response.status}: ${response.statusText}`;
        } else {
          this.successMessage = `¡Registro exitoso para ${responseData.usuario.first_name}! Ahora puedes iniciar sesión.`;
          this.formData = { id_morelia: '', email: '', password: '', confirm_password: '', first_name: '', last_name: '' };
          // this.$router.push('/login');
        }
      } catch (error) {
        console.error("Error during registration:", error); // Anglicized log
        this.apiError = "Could not connect to the server. Please try again later."; // Anglicized user message
      } finally {
        this.loading = false;
      }
    }
  }
}
</script>

<style scoped>
.register-page { /* Renamed class */
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.register-page h2 { /* Renamed class */
  text-align: center;
  color: #333;
  margin-bottom: 1.5rem;
}

/* Assuming .common-form, .form-group, .form-control, .button, .button-primary, .error-message, .success-message are defined globally or in App.vue */
.api-feedback-error, .api-feedback-success { /* Renamed classes for specificity */
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

.button {
  width: 100%;
  margin-top: 1rem;
}
</style>
