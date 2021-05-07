<template>
  <v-app dark>
    <v-app-bar app color="deep-purple darken-3" dark>
      <router-link style="text-decoration: none; color: inherit" to="/">
        <div class="d-flex align-center">
          <v-icon large> mdi-youtube </v-icon>
          <h2 class="ml-2 hidden-sm-and-down">
            YouTube <span class="font-weight-light">Prime</span>
          </h2>
        </div>
      </router-link>
      <v-spacer></v-spacer>
      <v-btn to="/dashboard" text>Dashboard</v-btn>
      <v-btn to="/account" text>Account</v-btn>
      <v-btn @click="logout" text>Logout</v-btn>
      <v-divider class="mx-3" vertical />
      <v-btn to="/upload" class="mr-1" title="Upload Video" icon>
        <v-icon>mdi-upload</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-slide-y-reverse-transition hide-on-leave>
        <router-view />
      </v-slide-y-reverse-transition>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),
  methods: {
    logout() {
      if (this.$store.state.accessToken != null) {
        this.$store.commit("destroyToken");
        this.$router.push({ name: "Login" });
      }
    },
  },
};
</script>
