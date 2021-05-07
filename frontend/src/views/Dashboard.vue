<template>
	<v-container class="mt-5">
		<v-btn @click="getVideos">Get videos</v-btn>
		<v-btn to="/channel/aturing">Channel</v-btn>
		<v-card color="deep-purple" class="pa-2">
			<v-card-text class="white--text mt-1">
				<h1>Welcome back, mneelansh! 🎉</h1>

				<div class="mt-3">
					<router-link to="/account">Account settings</router-link>
				</div>
			</v-card-text>
		</v-card>

		<v-form @submit.prevent="" class="mt-5">
			<v-text-field
				type="text"
				v-model="search_term"
				placeholder="Search channels"
				solo
			></v-text-field>
		</v-form>

		<div class="mt-2">
			<h1>Recommended videos</h1>
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
		<div class="mt-2">
			<h1>Recommended channels</h1>
			<v-row class="mt-5">
				<v-col cols="12" md="4" v-for="channel in topChannels" :key="channel.id">
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
import { mapState } from 'vuex'
import axios from 'axios'

export default {
	name: 'Dashboard',
	components: {},
	data: () => ({
		search_term: '',
		topChannels: [],
		vids: [],
	}),
	computed: mapState(['APIData']),
	methods: {
		getVideos() {
			//get token and channel_id from vuex
			let video_ids = []

			axios
				.post('http://127.0.0.1:5000/user-subscription', {
					idToken: this.$store.state.accessToken,
				})
				.then(res => {
					video_ids = res.data
					video_ids.forEach(element => {
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
			axios
				.post('http://127.0.0.1:5000/top-channels', {
					idToken: this.$store.state.accessToken,
				})
				.then(res => {
					let channels = res.data
					channels.forEach(element => {
						axios
							.post('http://127.0.0.1:5000/user', {
								user_id: element,
							})
							.then(res => {
								this.topChannels.push(res.data)
							})
					})
				})
		},
	},
}
</script>
