<template>
	<v-container>
		<div class="mx-5 mt-5">
			<div class="d-flex align-center">
				<v-avatar size="90">
					<v-img :src="user.photo_url" class="flex-grow-0" />
				</v-avatar>
				<div class="mt-4 ml-4">
					<h2 class="text-h4">{{ user.display_name }}</h2>
					<h3 class="text-overline">{{ user.email }}</h3>
				</div>
			</div>
		</div>
		<div v-if="vids.length !== 0" class="mt-2">
			<h1>Your videos</h1>
			<v-row class="mt-5">
				<v-col cols="12" md="4" v-for="vid in vids" :key="vid.id">
					<v-card>
						<v-img :aspect-ratio="16 / 9" :src="vid.thumbnail_url" />

						<v-card-title>{{ vid.title }} </v-card-title>
						<v-card-subtitle>
							{{ vid.description }}
						</v-card-subtitle>

						<v-card-actions>
							<v-btn
								color="deep-purple darken-3"
								:to="'/channel/' + vid.channel_id + '/' + vid.uid"
							>
								<v-icon>mdi-play</v-icon>
							</v-btn>
							<v-btn color="red darken-2" v-on:click="deleteVideo(vid.uid)">
								<v-icon>mdi-delete</v-icon>
							</v-btn>
						</v-card-actions>
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
			user: {},
		}
	},
	mounted() {
		this.getVideos()
		this.getSubscriptions()
		this.getUserData()
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
		async deleteVideo(inputVideoId) {
			await axios
				.post('http://127.0.0.1:5000/delete-video', {
					video_id: inputVideoId,
					idToken: this.$store.state.accessToken,
				})
				.then(res => {
					console.log(res.data)
				})
			this.getVideos()
		},
		getUserData() {
			axios
				.post('http://127.0.0.1:5000/user', {
					idToken: this.$store.state.accessToken,
				})
				.then(res => {
					this.user = res.data
					console.log(this.user)
				})
		},
	},
}
</script>

<style></style>
