<template>
	<div>
		<v-container class="mt-5">
			<h1>channel name {{ $route.params.id }}</h1>
			<v-btn @click="subscribe">
				<v-icon>{{ this.icon }}</v-icon>
			</v-btn>
			<v-btn @click="checkStatus">Check</v-btn>
			<v-btn @click="getVideos">getVideo</v-btn>

			<v-btn v-if="videos" :to="'/channel/' + $route.params.id + '/' + videos[0][1]">First vid</v-btn>
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
			channel_id: this.$route.params.id,
			icon: 'mdi-plus',
			videos: null
		}
	},
	methods: {
		checkStatus() {
			axios
				.post('http://127.0.0.1:5000/getAllSubsriptions', {
					idToken: this.$store.state.accessToken,
				})
				.then(res => {
					let channels = res.data
					console.log(channels)
					console.log(this.channel_id)
					if (channels.includes(this.channel_id)) {
						this.icon = 'mdi-check'
					} else {
						this.icon = 'mdi-plus'
					}
				})
		},
		async subscribe() {
			this.checkStatus()
			if (this.icon == 'mdi-plus') {
				await axios
					.post('http://127.0.0.1:5000/subscribe', {
						idToken: this.$store.state.accessToken,
						channel_id: this.$route.params.id,
					})
					.then(res => {
						console.log(res.data)
					})
			} else {
				await axios
					.post('http://127.0.0.1:5000/remove-subscription', {
						idToken: this.$store.state.accessToken,
						channel_id: this.$route.params.id,
					})
					.then(res => {
						console.log(res.data)
					})
			}
			this.checkStatus()
		},
		getVideos() {
			if (this.icon == 'mdi-plus') {
				console.log('Not subscribed')
			} else {
				axios
					.post('http://127.0.0.1:5000/getAllChannelVideos', {
						channel_id: this.$route.params.id,
					})
					.then(res => {
						this.videos = res.data
						console.log(res.data)
					})
			}
		},
	},
}
</script>

<style></style>
