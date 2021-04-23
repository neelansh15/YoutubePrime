import { createRouter, createWebHistory } from 'vue-router'

import Home from '../pages/Home.vue'
import Register from '../pages/Register.vue'

const routes = [
    {path: '/', component: Home},
    {path: '/register', component: Register},
]

export default createRouter({
    history: createWebHistory(),
    routes
})

