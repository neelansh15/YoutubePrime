<template>
	<v-container>
		<h1 class="mt-3">Account</h1>
		<v-btn @click="getVideos">Videos</v-btn>
		<v-btn @click="logout">Log out</v-btn>
	</v-container>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			name: 'Account',
			vid: [],
			videos: [],
		}
	},
	methods: {
		getVideos() {
			axios
				.post('http://127.0.0.1:5000/getAllChannelVideos', {
					channel_id_token: this.$store.state.accessToken,
				})
				.then(res => {
					this.videos = res.data
					console.log(this.videos)
					this.videos.forEach(element => {
						console.log(element)
						axios
							.post('http://127.0.0.1:5000/video-meta', {
								channel_id: element[0],
								video_id: element[1],
							})
							.then(res => {
								this.vid.push(res.data)
							})
					})
				})
		},
		logout() {
			this.$store.commit('destroyToken')
			this.$router.push({ name: 'Login' })
		},
	},
}
</script>

<style></style>
