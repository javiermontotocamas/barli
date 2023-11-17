import { FontAwesomeIcon } from './plugins/fontawesome';
import './assets/main.css'
import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap/dist/js/bootstrap.bundle.min.js'
// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon);  // Registra el componente globalmente
app.use(router)
app.mount('#app')


