<template>
	<v-container class="mt-5">
		<v-btn @click="getVideos">TESt</v-btn>
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
					<v-card :to="'/play/' + vid.id">
						<v-img :aspect-ratio="16 / 9" :src="vid.thumbnail" />
						<v-card-title>{{ vid.title }}</v-card-title>
						<v-card-subtitle>{{ vid.description }}</v-card-subtitle>
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
		vids: [
			{
				id: 1,
				title: 'Video title',
				description: 'Video description',
				thumbnail:
					'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80',
			},
			{
				id: 2,
				title: 'Video title',
				description: 'Video description',
				thumbnail:
					'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80',
			},
			{
				id: 3,
				title: 'Video title',
				description: 'Video description',
				thumbnail:
					'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80',
			},
			{
				id: 4,
				title: 'Video title',
				description: 'Video description',
				thumbnail:
					'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80',
			},
			{
				id: 5,
				title: 'Video title',
				description: 'Video description',
				thumbnail:
					'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80',
			},
			{
				id: 6,
				title: 'Video title',
				description: 'Video description',
				thumbnail:
					'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80',
			},
		],
	}),
	computed: mapState(['APIData']),
	methods: {
		getVideos() {
			//get token and channel_id from vuex
			let video_ids = []

			let token =
				'eyJhbGciOiJSUzI1NiIsImtpZCI6ImNjM2Y0ZThiMmYxZDAyZjBlYTRiMWJkZGU1NWFkZDhiMDhiYzUzODYiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiTmV3IFVzZXIgMiIsInBpY3R1cmUiOiJodHRwczovL2ltYWdlcy51bnNwbGFzaC5jb20vcGhvdG8tMTUxMTM2NzQ2MTk4OS1mODVhMjFmZGExNjc_aXhpZD1Nbnd4TWpBM2ZEQjhNSHh6WldGeVkyaDhNbng4Y0hKdlptbHNaWHhsYm53d2ZId3dmSHclM0QmaXhsaWI9cmItMS4yLjEmdz0xMDAwJnE9ODAiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcHJpbWUtNDNjMDUiLCJhdWQiOiJwcmltZS00M2MwNSIsImF1dGhfdGltZSI6MTYyMDMxNTkxMywidXNlcl9pZCI6ImpBWWt1TTNhM1BjZnFrMHZnYXBzTmVPeVhLNTIiLCJzdWIiOiJqQVlrdU0zYTNQY2ZxazB2Z2Fwc05lT3lYSzUyIiwiaWF0IjoxNjIwMzE1OTEzLCJleHAiOjE2MjAzMTk1MTMsImVtYWlsIjoibmV3dXNlcjJAZXhhbXBsZS5jb20iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZW1haWwiOlsibmV3dXNlcjJAZXhhbXBsZS5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCJ9fQ.B3m-1h2ZpcUMuHfvXCASXDFdWEqXZz71MgkEHbNmz-9cAGjgKbkCmN3iBxGMnNQns5QWOagOxJw7onjEp8Kz2Is3cpQC--gea9TF8sYuMYvt0wm9BU7qwMf-lelaM2rVBtkV2C12NyDaX3pc31gH3_NMlNOB2fjhwCNe4Xv6sr2XgbZsdBlTu2MEv1ZppQzsld332kK5bv6Dk81-twm-0rl4nZZ4GgrmU-k2oSglhWLh53IC4EkKwEyWN0mIIiPqYI-qunK4KziWkWNW6kSAAi-Q6airOtcEqrTiinA_oufwReUmAwZlb49IgXuClAq3-L8ZaeZGaJ-VLczcMZwzpg'
			axios
				.post('http://127.0.0.1:5000/user-subscription', {
					idToken: token,
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
								console.log(res.data)
							})
					})
				})
		},
	},
}
</script>
