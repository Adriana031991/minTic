import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'nprogress/nprogress.css'
import { createPinia } from 'pinia'
import 'materialize-css/dist/css/materialize.min.css'
import 'material-design-icons/iconfont/material-icons.css'


createApp(App).
use(router).
use(createPinia()).
mount('#app')
