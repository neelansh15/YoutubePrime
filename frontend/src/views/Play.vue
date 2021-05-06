<template>
	<div>
		<h1>Play</h1>
		<h2>{{ $route.params.id }}</h2>
		<h2>{{ $route.params.videoid }}</h2>
		<h3>{{ $store.state.accessToken }}</h3>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'Play',
	mounted(){
		axios.post("http://localhost:5000/getVideo", {
			idToken: this.$store.state.accessToken,
			channel_id: this.$route.params.id,
			video_id: this.$route.params.videoid
		})
	}
}
</script>

<style></style>
