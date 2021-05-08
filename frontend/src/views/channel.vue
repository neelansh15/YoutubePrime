<template>
	<div>
		<v-container class="mt-5">
			<div class="mx-5 mt-5">
				<div class="d-flex align-center">
					<v-avatar size="90">
						<v-img :src="chanenl_photo" class="flex-grow-0" />
					</v-avatar>
					<div class="mt-4 ml-4">
						<h2 class="text-h4">{{ this.channel_name }}</h2>
						<h3 class="text-overline">{{ this.subscribers }} subscribers</h3>
					</div>
				</div>
			</div>

			<v-btn
				class="mt-3 ml-10"
				:color="this.icon == 'mdi-plus' ? 'purple darken-3' : ''"
				@click="subscribe"
			>
				<v-icon class="mr-2">{{ this.icon }}</v-icon>
				{{ this.buttonText }}
			</v-btn>

			<div v-if="vids.length !== 0" class="mt-2">
				<h1>Channel videos</h1>
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
		</v-container>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			channel_id: this.$route.params.id,
			icon: 'mdi-plus',
			videos: null,
			chanenl_photo: '',
			channel_name: '',
			vids: [],
			buttonText: ' Subscribe',
			subscribers: 0,
		}
	},
	async mounted() {
		console.log(this.channel_id)
		await axios
			.post('http://127.0.0.1:5000/getAllSubsriptions', {
				idToken: this.$store.state.accessToken,
			})
			.then(res => {
				let channels = res.data
				console.log(channels)
				console.log(this.channel_id)
				if (channels.includes(this.channel_id)) {
					this.icon = 'mdi-check'
					this.buttonText = ' Subscribed'
				} else {
					this.icon = 'mdi-plus'
					this.buttonText = ' Subscribe'
				}
			})
		await this.getChannelDetails()
		this.getVideos()
	},
	methods: {
		async getChannelDetails() {
			await axios
				.post('http://127.0.0.1:5000/user', {
					user_id: this.channel_id,
				})
				.then(res => {
					this.chanenl_photo = res.data.photo_url
					this.channel_name = res.data.display_name
					this.subscribers = res.data.subscriber_count
				})
		},
		async subscribe() {
			if (this.icon == 'mdi-plus') {
				await axios
					.post('http://127.0.0.1:5000/subscribe', {
						idToken: this.$store.state.accessToken,
						channel_id: this.$route.params.id,
					})
					.then(res => {
						console.log(res.data)
					})
				this.icon = 'mdi-check'
				this.buttonText = ' Subscribed'
				this.subscribers += 1
			} else {
				await axios
					.post('http://127.0.0.1:5000/remove-subscription', {
						idToken: this.$store.state.accessToken,
						channel_id: this.$route.params.id,
					})
					.then(res => {
						console.log(res.data)
					})
				this.icon = 'mdi-plus'
				this.buttonText = ' Subscribe'
				this.subscribers -= 1
			}
			this.getVideos()
		},
		getVideos() {
			if (this.icon == 'mdi-plus') {
				console.log('Not subscribed')
				this.vids = []
			} else {
				axios
					.post('http://127.0.0.1:5000/getAllChannelVideos', {
						channel_id: this.$route.params.id,
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
			}
		},
	},
}
</script>

<style></style>
