import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

// if a page needs user to be logged in
// if the user isnt logged in redirect to login page

router.beforeEach((to, from, next) => {
	if (to.matched.some(record => record.meta.requiresLogin)) {
		if (!store.getters.loggedIn) {
			next({ name: 'Login' })
		} else {
			next()
		}
	} else {
		next()
	}
})

new Vue({
	router,
	store,
	vuetify,
	render: h => h(App),
}).$mount('#app')
