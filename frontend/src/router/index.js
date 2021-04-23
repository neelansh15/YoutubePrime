import { createRouter, createWebHistory } from 'vue-router'

import Home from '../pages/Home'
import Register from '../pages/Register'

const routes = [
    {path: '/home', component: Home},
    {path: '/register', component: Register},
]

export default createRouter({
    history: createWebHistory(),
    routes
})

