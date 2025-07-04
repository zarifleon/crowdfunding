<template>
  <nav class="navigation-bar"> <!-- Renamed class -->
    <div class="nav-brand"> <!-- Renamed class -->
      <router-link to="/">CrowdMorelia</router-link>
    </div>
    <ul class="nav-links"> <!-- Renamed class -->
      <li>
        <router-link to="/">Home</router-link> <!-- Anglicized -->
      </li>
      <li v-if="!isAuthenticated"> <!-- Renamed computed property -->
        <router-link to="/register">Register</router-link> <!-- Anglicized -->
      </li>
      <li v-if="!isAuthenticated"> <!-- Renamed computed property -->
        <router-link to="/login">Login</router-link> <!-- Anglicized -->
      </li>
      <li v-if="isAuthenticated"> <!-- Renamed computed property -->
        <router-link to="/create-case">Create Case</router-link> <!-- Anglicized -->
      </li>
      <li v-if="isAuthenticated"> <!-- Renamed computed property -->
        <router-link to="/profile">My Profile</router-link> <!-- Anglicized -->
      </li>
      <li v-if="isAuthenticated"> <!-- Corrected v-if, Renamed computed property -->
        <button @click="handleLogout" class="button-logout">Logout</button> <!-- Anglicized, Renamed method -->
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'NavigationBar', // Renamed component
  // In a real application, authentication status would come from Vuex or an auth service.
  // For now, this is a placeholder.
  data() {
    return {
      // To easily test UI, toggle this value in code or via Vue Devtools (if available):
      // In a real app, this would come from a global store (Vuex/Pinia)
      // or be determined by the presence of an auth token.
      internalIsAuthenticated: false, // <<-- TOGGLE THIS FOR TESTING (true/false)
    };
  },
  computed: {
    isAuthenticated() {
      // In a real app: return this.$store.state.auth.isAuthenticated;
      return this.internalIsAuthenticated;
    }
  },
  methods: {
    handleLogout() {
      console.log("Logout handler called");
      // In a real app:
      // this.$store.dispatch('auth/logoutAction'); // Example if using Vuex/Pinia
      // this.$router.push('/login');
      this.internalIsAuthenticated = false; // Simulate logout for local testing
      alert("Simulated Logout. User is now logged out for UI testing purposes in NavigationBar.");
    },
    // Example method to simulate login, could be called from devtools or other test setup
    _simulateLogin() {
        this.internalIsAuthenticated = true;
         alert("Simulated Login in NavigationBar.");
    }
  }
}
</script>

<style scoped>
.navigation-bar {
  background-color: #343a40;
  padding: 0.75rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: white;
}

.nav-brand a { /* Renamed class */
  color: white;
  text-decoration: none;
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-links { /* Renamed class */
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  align-items: center;
}

.nav-links li { /* Renamed class */
  margin-left: 1.5rem;
}

.nav-links a { /* Renamed class */
  color: #adb5bd;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.2s ease-in-out;
}

.nav-links a:hover, /* Renamed class */
.nav-links a.router-link-exact-active { /* Renamed class */
  color: white;
}

.button-logout { /* Renamed class */
  background-color: transparent;
  color: #adb5bd;
  border: 1px solid #adb5bd;
  padding: 0.375rem 0.75rem;
  border-radius: 0.25rem;
  cursor: pointer;
  font-size: 1rem;
  transition: color 0.2s ease-in-out, background-color 0.2s ease-in-out;
}

.button-logout:hover { /* Renamed class */
  color: white;
  background-color: #495057;
}
</style>
