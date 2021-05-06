<template>
	<div>
		<h1>Play</h1>
		<h2>{{ $route.params.id }}</h2>
		<h2>{{ $route.params.videoid }}</h2>
		<h3>{{ $store.state.accessToken }}</h3>

		<video v-if="video_url" :src="video_url" :type="'video/' + video_type" controls />
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: 'Play',
	data: () => ({
		video_url: null
	}),
	mounted(){
		axios.post("http://localhost:5000/getVideo", {
			idToken: this.$store.state.accessToken,
			channel_id: this.$route.params.id,
			video_id: this.$route.params.videoid
		})
		.then((res) => {
			console.log(res)
			if(res.data == 'Unauthorized' || res.status != 200){
				this.$router.push(`/channel/${this.$route.params.id}`)
			}
			else{
				this.video_url = res.data[0]
				this.video_type = res.data[1].type
			}
		})
	}
}
</script>

<style></style>
