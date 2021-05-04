import Vue from 'vue'
import Vuex from 'vuex'
// import { getAPI } from '../axios-api'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		accessToken: null,
		refreshToken: null,
		APIData: '',
	},
	mutations: {
		updateStorage(state, { access, refresh }) {
			state.accessToken = access
			state.refreshToken = refresh
		},
		destroyToken(state) {
			state.accessToken = null
			state.refreshToken = null
		},
	},
	getters: {
		loggedIn(state) {
			return state.accessToken != null
		},
	},
	actions: {
		// userLogin(context, userCredintials) {
		// 	return new Promise(resolve => {
		// 		getAPI
		// 			.post('/auth/api-token/', {
		// 				username: userCredintials.username,
		// 				password: userCredintials.password,
		// 			})
		// 			.then(response => {
		// 				context.commit('updateStorage', {
		// 					access: response.data.access,
		// 					refresh: response.data.refresh,
		// 				})
		// 				resolve()
		// 			})
		// 	})
		// },
		userLogout(context) {
			if (context.getters.loggedIn) {
				context.commit('destroyToken')
			}
		},
	},
	modules: {},
})
