<template>
	<v-container>
		<h1 class="mt-3">Account</h1>
		<v-btn @click="getVideos">Videos</v-btn>
		<v-btn @click="getSubscriptions">Channels</v-btn>
		<v-btn @click="logout">Log out</v-btn>
		<div v-if="vids.length !== 0" class="mt-2">
			<h1>Your videos</h1>
			<v-row class="mt-5">
				<v-col cols="12" md="4" v-for="vid in vids" :key="vid.id">
					<v-card :to="'/channel/' + vid.channel_id + '/' + vid.uid">
						<v-img :aspect-ratio="16 / 9" :src="vid.thumbnail_url" />
						<v-card-title>{{ vid.title }}</v-card-title>
						<v-card-subtitle>{{ vid.description }}</v-card-subtitle>
					</v-card>
				</v-col>
			</v-row>
		</div>
		<div v-if="channelsData.length !== 0" class="mt-2">
			<h1>Subscribed channels</h1>
			<v-row class="mt-5">
				<v-col cols="12" md="4" v-for="channel in channelsData" :key="channel.id">
					<v-card :to="'/channel/' + channel.uid">
						<v-img :aspect-ratio="16 / 9" :src="channel.photo_url" />
						<v-card-title>{{ channel.display_name }}</v-card-title>
						<v-card-subtitle
							>{{ channel.subscriber_count }} subscribers</v-card-subtitle
						>
					</v-card>
				</v-col>
			</v-row>
		</div>
	</v-container>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			name: 'Account',
			vids: [],
			videos: [],
			channels: [],
			channelsData: [],
		}
	},
	methods: {
		getVideos() {
			this.vids = []
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
								this.vids.push(res.data)
							})
					})
				})
		},
		getSubscriptions() {
			this.channelsData = []
			axios
				.post('http://127.0.0.1:5000/getAllSubsriptions', {
					idToken: this.$store.state.accessToken,
				})
				.then(res => {
					this.channels = res.data
					console.log(this.channels)
					this.channels.forEach(element => {
						console.log(element)
						axios
							.post('http://127.0.0.1:5000/user', {
								user_id: element,
							})
							.then(res => {
								this.channelsData.push(res.data)
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
