<template>
  <v-container class="mt-4">
    <h1>Upload a new video</h1>

    <!-- Dropzone element -->
    <dropzone ref="dropzone" :options="dropzoneOptions" duplicateCheck />
    <v-form class="mt-5" ref="form" @submit.prevent="">
      <v-text-field :counter="50" label="Title"></v-text-field>
      <v-textarea label="Description" :counter="200"></v-textarea>
    </v-form>
  </v-container>
</template>

<script>
import dropzone from "vue2-dropzone";

export default {
  name: "Upload",
  components: {
    dropzone,
  },
  data: () => ({
    dropzoneOptions: {
       url: 'https://httpbin.org/post',
      thumbnailWidth: 150,
      maxFilesize: 0.5,
      headers: { "My-Awesome-Header": "header value" },
    },
  }),
};
</script>

<style>
</style>