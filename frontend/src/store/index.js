import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
	plugins: [createPersistedState()],
	state: {
		baseURL: 'http://localhost:5000',
		accessToken: null,
		refreshToken: null,
		APIData: '',
	},
	mutations: {
		setToken(state, payload) {
			state.accessToken = payload
		},
		destroyToken(state) {
			state.accessToken = null
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
		logout(context) {
			if (context.getters.loggedIn) {
				context.commit('destroyToken')
			}
		},
	},
	modules: {},
})
