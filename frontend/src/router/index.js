import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Home from '../views/Home.vue'
import Play from '../views/Play.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import PlayOwner from '../views/PlayOwner.vue'
import Video from '../views/Video.vue'
import Upload from '../views/Upload.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
	},
	{
		path: '/dashboard',
		name: 'Dashboard',
		component: Dashboard,
	},
	{
		path: '/play',
		name: 'Play',
		component: PlayOwner,
		children: [
			{
				path: '/play/:id',
				name: 'Play',
				component: Play,
			},
		],
	},
	{
		path: '/login',
		name: 'Login',
		component: Login,
	},
	{
		path: '/register',
		name: 'Register',
		component: Register,
	},
	{
		path: '/upload',
		name: 'Upload',
		component: Upload,
	},
	{
		path: '/account',
		name: 'Account',
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		component: () =>
			import(/* webpackChunkName: "about" */ '../views/Account.vue'),
	},
	{
		path: '/video',
		name: 'video',
		component: Video,

	},
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
})

export default router
