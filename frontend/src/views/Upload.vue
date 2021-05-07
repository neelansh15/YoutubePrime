<template>
	<v-container class="mt-4">
		<v-alert type="success" v-if="progress == 1">Uploaded</v-alert>
		<v-progress-linear
			v-show="progress != 0 && progress != 1"
			:value="progress * 100"
		></v-progress-linear>
		<h1 class="mt-3">Upload a new video</h1>
		<v-form class="mt-5" ref="form" @submit.prevent="upload">
			Video:
			<v-file-input
				name="myfile"
				v-model="myfile"
				accept="video/*"
				show-size
			></v-file-input>
			Thumbnail:
			<v-file-input
				name="thumbnail"
				v-model="thumbnail"
				accept="image/*"
				show-size
			></v-file-input>
			<v-text-field :counter="50" label="Title" v-model="title"></v-text-field>
			<v-textarea
				label="Description"
				:counter="200"
				v-model="description"
			></v-textarea>
			<v-btn type="submit" class="primary">Upload</v-btn>
			<!-- <v-btn class="secondary">Cancel</v-btn> -->
		</v-form>
	</v-container>
</template>

<script>
import axios from 'axios'

export default {
	name: 'Upload',
	data: () => ({
		myfile: null,
		thumbnail: null,
		title: '',
		description: '',
		progress: 0,
	}),
	methods: {
		upload() {
			let formData = new FormData()
			formData.append('myfile', this.myfile)
			formData.append('thumbnail', this.thumbnail)
			formData.append('title', this.title)
			formData.append('description', this.description)
			formData.append('idToken', this.$store.state.accessToken)
			axios
				.post(this.$store.state.baseURL + '/upload', formData, {
					headers: {
						'Content-Type': 'multipart/form-data',
					},
					onUploadProgress: e => {
						console.log(e)
						this.progress = ((e.loaded / e.total) * 80) / 100
					},
				})
				.then(res => {
					console.log(res)
					this.progress = 1
				})
		},
	},
}
</script>

<style></style>
