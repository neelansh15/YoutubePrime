<template>
	<div>
		<v-card>
			<v-row>
				channel name
			</v-row>
			<v-row>
				<v-btn @click="subscribe"></v-btn>
			</v-row>
		</v-card>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			channel_id: '',
		}
	},
	methods: {
		subscribe() {
			let token = 'GETTOKENFROMVUEX'
			let channel_id = 'GETCHANNELIDFROMVUEX'
			axios
				.post('http://127.0.0.1:5000/subscribe', {
					idToken: token,
					channel_uid: channel_id,
				})
				.then(res => {
					console.log(res.data)
				})
		},
	},
}
</script>

<style></style>
