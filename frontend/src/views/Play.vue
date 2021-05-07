<template>
  <v-container class="pt-10">
    <v-fade-transition>
      <div v-if="video_doc == null">
        <h1>Loading...</h1>
      </div>
      <div v-else>
        <v-btn @click="$router.go(-1)" class="mb-3" plain>&larr; Back</v-btn>
		<br />
        <video
          v-if="video_url"
          :src="video_url"
          :type="'video/' + video_type"
          controls
          width="854"
          height="480"
        />

        <h1 class="mt-3">{{ video_doc.title }}</h1>
        <p>{{ video_doc.description }}</p>
        <!-- <v-img :aspect-ratio="16/9" width="426" :src="video_doc.thumbnail_url" /> -->
      </div>
    </v-fade-transition>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Play",
  data: () => ({
    video_url: null,
    video_doc: null,
  }),
  mounted() {
    axios
      .post("http://localhost:5000/getVideo", {
        idToken: this.$store.state.accessToken,
        channel_id: this.$route.params.id,
        video_id: this.$route.params.videoid,
      })
      .then((res) => {
        console.log(res);
        if (res.data == "Unauthorized" || res.status != 200) {
          this.$router.push(`/channel/${this.$route.params.id}`);
        } else {
          this.video_url = res.data[0];
          this.video_doc = res.data[1];
        }
      });
  },
};
</script>

<style></style>
