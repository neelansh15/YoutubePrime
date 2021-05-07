<template>
	<div>
		<v-container class="mt-5">
			<v-row no-gutters>
				<v-col>
					<h1>{{ this.channel_name }}</h1>
				</v-col>
				<v-col>
					<v-btn @click="subscribe">
						<v-icon>{{ this.icon }}</v-icon>
					</v-btn>
				</v-col>
			</v-row>

			<v-btn @click="getVideos">getVideo</v-btn>

			<v-btn
				v-if="videos"
				to="/channel/jAYkuM3a3Pcfqk0vgapsNeOyXK52/FSAvG1WkiUWC2EB53JZo"
				>First vid</v-btn
			>
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
			channel_name: '',
		}
	},
	mounted() {
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
		axios
			.post('http://127.0.0.1:5000/user', {
				user_id: this.channel_id,
			})
			.then(res => {
				this.channel_name = res.data.display_name
			})
	},
	methods: {
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
			}
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
						console.log(this.videos)
						this.videos.forEach(element => {
							console.log(element)
							axios
								.post('http://127.0.0.1:5000/video-meta', {
									channel_id: element[0],
									video_id: element[1],
								})
								.then(res => {
									console.log(res.data)
								})
						})
					})
			}
		},
	},
}
</script>

<style></style>
