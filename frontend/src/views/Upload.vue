<template>
  <v-container class="mt-4">
    <h1>Upload a new video</h1>

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
      <v-btn class="primary">Upload</v-btn>
      <!-- <v-btn class="secondary">Cancel</v-btn> -->
    </v-form>
  </v-container>
</template>

<script>
// import axios from "axios";

export default {
  name: "Upload",
  components: {
    // dropzone,
  },
  data: () => ({
    myfile: null,
    thumbnail: null,
    title: "",
    description: "",
  }),
  methods: {
    upload(e) {
      console.log(e);

      let formData = new FormData();
      formData.append("myfile", this.myfile);
      formData.append("thumbnail", this.thumbnail);
      formData.append("title", this.title);
      formData.append("description", this.description);
	console.log(formData)
    //   axios.post(this.$store.state.baseURL + "/upload", formData, {
    //     headers: {
    //       "Content-Type": "multipart/form-data",
    //     },
    //     onUploadProgress: (e) => {
    //       console.log(e);
    //     },
    //   });
    },
    onUploadProgress(e) {
      console.log("Upload progress: ");
      console.log(e);
    },
  },
};
</script>

<style></style>
