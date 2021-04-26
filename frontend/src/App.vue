<template>
  <v-app dark>
    <v-app-bar app color="deep-purple darken-3" dark>
      <router-link style="text-decoration: none; color: inherit" to="/">
        <div class="d-flex align-center">
          <v-icon large> mdi-youtube </v-icon>
          <h2 class="ml-2 hidden-sm-and-down">
            Youtube <span class="font-weight-light">Prime</span>
          </h2>
        </div>
      </router-link>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <router-view />
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
};
</script>
