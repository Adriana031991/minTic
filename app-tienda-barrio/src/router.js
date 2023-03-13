import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import LogIn from './components/Login.vue'
import SingUp from './components/SingUp.vue'
import Home from './components/Home.vue'
import Account from './components/Account.vue'

const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },
  {
    path: '/user/logIn',
    name: 'logIn',
    component: LogIn
  },
  {
    path: '/user/singUp',
    name: 'signUp',
    component: SingUp
  },
  {
    path: '/user/home',
    name: 'home',
    component: Home
  },
  {
    path: '/user/account',
    name: "account",
    component: Account
    }

]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
