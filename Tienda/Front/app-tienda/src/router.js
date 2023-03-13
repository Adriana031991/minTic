import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import LogIn from './components/Login.vue'
import SingUp from './components/SingUp.vue'
import Home from './components/Home.vue'
import Account from './components/Account.vue'
import Products from './components/Productos.vue'
import Sales from './components/Sales.vue'
import Bill from './components/Bill.vue'

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
    path: '/productos',
    name: "Productos",
    component: Products
  },
  {
    path: '/sales',
    name: "Sales",
    component: Sales
  },
  {
    path: '/bill',
    name: "Bill",
    component: Bill
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/account',
    name: "account",
    component: Account
  },
  

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
