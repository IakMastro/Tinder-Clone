import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from "bootstrap-vue";
import axios from "axios";

Vue.use(BootstrapVue)

axios.defaults.headers.common['Access-Control-Allow-Origins'] = '*';

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
