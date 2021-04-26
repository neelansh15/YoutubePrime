import { createApp } from 'vue'
import App from './App.vue'

import PrimeVue from 'primevue/config'
import Button from 'primevue/button'

import router from './router'

const app = createApp(App)

app.use(router)

app.use(PrimeVue)

app.component('Button', Button)


app.mount('#app')
