<template>
	<div>
		<v-container class="mt-5">
			<h1>channel name {{ $route.params.id }}</h1>
			<v-btn @click="subscribe"
				><v-icon>{{ this.icon }}</v-icon></v-btn
			>
		</v-container>
		<!-- <v-card>
			<v-row> channel name {{ $route.params.id }} </v-row>
			<v-row>
			</v-row>
		</v-card> -->
	</div>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			channel_id: '',
			icon: 'mdi-plus',
		}
	},
	methods: {
		checkStatus() {},
		subscribe() {
			axios
				.post('http://127.0.0.1:5000/subscribe', {
					idToken: this.$store.state.authToken,
					channel_uid: this.$route.params.id,
				})
				.then(res => {
					console.log(res.data)
				})
		},
	},
}
</script>

<style></style>
