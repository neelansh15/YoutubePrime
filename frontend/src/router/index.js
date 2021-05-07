import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Home from '../views/Home.vue'
import Play from '../views/Play.vue'
import Login from '../views/Login.vue'
import Logout from '../views/Logout.vue'
import Register from '../views/Register.vue'
import Video from '../views/Video.vue'
import Upload from '../views/Upload.vue'
import Channel from '../views/channel.vue'
import ChannelViewsOwner from '../views/ChannelViewsOwner.vue'
import ChannelOwner from '../views/ChannelOwner.vue'

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
		meta: {
			requiresLogin: true,
		},
	},
	{
		path: '/login',
		name: 'Login',
		component: Login,
	},
	{
		path: '/logout',
		name: 'Logout',
		component: Logout,
		meta: {
			requiresLogin: true,
		},
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
		meta: {
			requiresLogin: true,
		},
	},
	{
		path: '/channel',
		name: 'ChannelOwner',
		component: ChannelOwner,
		children: [
			{
				path: '/channel/:id',
				name: 'ChannelViewsOwner',
				component: ChannelViewsOwner,
				children: [
					{
						path: '/',
						name: 'Channel',
						component: Channel,
					},
					{
						path: '/channel/:id/:videoid',
						name: 'ChannelVideo',
						component: Play,
					},
				],
			},
		],
		// meta: {
		// 	requiresLogin: true,
		// },
	},
	{
		path: '/account',
		name: 'Account',
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		component: () =>
			import(/* webpackChunkName: "about" */ '../views/Account.vue'),
		meta: {
			requiresLogin: true,
		},
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
