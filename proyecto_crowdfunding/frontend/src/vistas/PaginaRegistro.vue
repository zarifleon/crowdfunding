<template>
  <div class="pagina-registro">
    <h2>Registro de Nuevo Usuario</h2>
    <form @submit.prevent="manejarRegistro" class="formulario-comun">
      <div class="form-grupo">
        <label for="id_morelia">ID Morelia (CURP o Identificador Único):</label>
        <input type="text" id="id_morelia" v-model="formData.id_morelia" required class="form-control">
      </div>
      <div class="form-grupo">
        <label for="email">Correo Electrónico:</label>
        <input type="email" id="email" v-model="formData.email" required class="form-control">
      </div>
      <div class="form-grupo">
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="formData.password" required class="form-control">
      </div>
      <div class="form-grupo">
        <label for="confirmar_password">Confirmar Contraseña:</label>
        <input type="password" id="confirmar_password" v-model="formData.confirmar_password" required class="form-control">
      </div>
      <div class="form-grupo">
        <label for="first_name">Nombres:</label>
        <input type="text" id="first_name" v-model="formData.first_name" required class="form-control">
      </div>
      <div class="form-grupo">
        <label for="last_name">Apellidos:</label>
        <input type="text" id="last_name" v.model="formData.last_name" required class="form-control">
      </div>

      <!-- Campos Opcionales (ejemplo: tipo de usuario, nivel) -->
      <!-- Estos podrían ser selectores cargados desde la API -->
      <!-- <div class="form-grupo">
        <label for="usuario_tipo_id">Tipo de Usuario (Opcional):</label>
        <input type="number" id="usuario_tipo_id" v-model="formData.usuario_tipo_id" class="form-control">
      </div> -->

      <div v-if="errorApi" class="mensaje-error api-error">
        {{ errorApi }}
      </div>
      <div v-if="mensajeExito" class="mensaje-exito api-exito">
        {{ mensajeExito }}
      </div>

      <button type="submit" :disabled="cargando" class="boton boton-primario">
        {{ cargando ? 'Registrando...' : 'Registrar Usuario' }}
      </button>
    </form>
  </div>
</template>

<script>
const API_BASE_URL = '/api/v1/crowdfunding';

export default {
  name: 'PaginaRegistro',
  data() {
    return {
      formData: {
        id_morelia: '',
        email: '',
        password: '',
        confirmar_password: '',
        first_name: '',
        last_name: '',
        // usuario_tipo_id: null, // Ejemplo opcional
      },
      cargando: false,
      errorApi: null,
      mensajeExito: null,
    };
  },
  methods: {
    async manejarRegistro() {
      this.cargando = true;
      this.errorApi = null;
      this.mensajeExito = null;

      if (this.formData.password !== this.formData.confirmar_password) {
        this.errorApi = "Las contraseñas no coinciden.";
        this.cargando = false;
        return;
      }

      // No enviar confirmar_password a la API
      const payload = { ...this.formData };
      delete payload.confirmar_password;

      try {
        const response = await fetch(`${API_BASE_URL}/usuarios/registrar/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            // CSRF token sería necesario aquí si no se usa @csrf_exempt en Django y se usan sesiones.
            // 'X-CSRFToken': 'token_csrf_obtenido_de_cookie_o_meta_tag'
          },
          body: JSON.stringify(payload),
        });

        const responseData = await response.json();

        if (!response.ok) {
          // Asumimos que la API devuelve errores en formato { "error": "mensaje" }
          this.errorApi = responseData.error || `Error ${response.status}: ${response.statusText}`;
        } else {
          this.mensajeExito = `¡Registro exitoso para ${responseData.usuario.first_name}! Ahora puedes iniciar sesión.`;
          // Limpiar formulario o redirigir
          this.formData = { id_morelia: '', email: '', password: '', confirmar_password: '', first_name: '', last_name: '' };
          // this.$router.push('/login'); // Redirigir a login después de éxito
        }
      } catch (error) {
        console.error("Error en el registro:", error);
        this.errorApi = "No se pudo conectar con el servidor. Intenta de nuevo más tarde.";
      } finally {
        this.cargando = false;
      }
    }
  }
}
</script>

<style scoped>
.pagina-registro {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.pagina-registro h2 {
  text-align: center;
  color: #333;
  margin-bottom: 1.5rem;
}

/* .formulario-comun (estilos globales en App.vue) se aplicarán aquí si es necesario */
/* Estilos específicos si son necesarios */
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
.api-exito {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.boton { /* Estilo para el botón de submit si no se hereda bien */
  width: 100%;
  margin-top: 1rem;
}
</style>
