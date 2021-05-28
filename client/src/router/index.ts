import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Account from '../components/Account.vue'
import Login from '../components/Login.vue'
import Prime from '../components/Prime.vue'
import Users from '../components/Users.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Users',
    component: Users
  },
  {
    path: '/settings',
    name: 'Account',
    component: Account
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/prime',
    name: 'Prime',
    component: Prime
  }
]

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
