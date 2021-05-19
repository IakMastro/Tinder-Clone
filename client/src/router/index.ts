import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Login from '../components/Login.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
]

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
