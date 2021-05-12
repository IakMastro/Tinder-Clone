import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Ping from '../components/Ping.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Ping',
    component: Ping
  },
]

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
