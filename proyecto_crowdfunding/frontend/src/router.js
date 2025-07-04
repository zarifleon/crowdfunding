// import { createRouter, createWebHistory } from 'vue-router'; // Actual import for Vue Router 4

// Import page components from the 'views' directory with their new English names
import HomePage from './views/HomePage.vue';
import RegisterPage from './views/RegisterPage.vue';
import LoginPage from './views/LoginPage.vue';
import CaseListPage from './views/CaseListPage.vue';
import CaseDetailPage from './views/CaseDetailPage.vue';
import CreateCasePage from './views/CreateCasePage.vue';

const NotFoundPage = { template: '<div><h2>404 - Page Not Found</h2><p>Sorry, the page you are looking for does not exist.</p><router-link to="/">Go to Home</router-link></div>' }; // Anglicized

const routes = [
  {
    path: '/',
    name: 'Home', // Anglicized
    component: HomePage,
  },
  {
    path: '/register', // Anglicized path
    name: 'Register', // Anglicized
    component: RegisterPage,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
  },
  {
    path: '/cases', // Anglicized path
    name: 'CaseList', // Anglicized
    component: CaseListPage,
  },
  {
    path: '/cases/:caseId', // Parameter name is fine as is
    name: 'CaseDetail', // Anglicized (matches CaseCard link)
    component: CaseDetailPage,
    props: true,
  },
  {
    path: '/create-case', // Anglicized path
    name: 'CreateCase', // Anglicized
    component: CreateCasePage,
    // meta: { requiresAuth: true } // Example for route guards
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound', // Anglicized
    component: NotFoundPage,
  }
];

// Esta es la creación del router. En una app real, se importaría createRouter y createWebHistory.
// const router = createRouter({
//   history: createWebHistory(process.env.BASE_URL || '/'), // process.env.BASE_URL es para Vue CLI
//   routes,
//   scrollBehavior(to, from, savedPosition) {
//     // Siempre desplazar al inicio al navegar a una nueva ruta, a menos que haya una posición guardada (navegación atrás/adelante)
//     if (savedPosition) {
//       return savedPosition;
//     } else {
//       return { top: 0, behavior: 'smooth' };
//     }
//   }
// });

// export default router;


// --- SIMULACIÓN PARA ENTORNO SIN VUE-ROUTER INSTALADO ---
// Simplemente exportamos las rutas para que puedan ser referenciadas,
// pero la creación real del router y su uso en main.js no se puede ejecutar aquí.
console.log("Archivo router.js cargado con definiciones de rutas.");
export const definidasRutas = routes; // Exportar las rutas para que main.js las pueda "ver" conceptualmente

// En un main.js real, se haría algo como:
// import { createApp } from 'vue'
// import App from './App.vue'
// import router from './router' // Importando la instancia del router
// const app = createApp(App)
// app.use(router) // Usando el router
// app.mount('#app')

// --- FIN SIMULACIÓN ---
