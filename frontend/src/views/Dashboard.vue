<template>
  <v-container class="mt-5">
    <v-card color="deep-purple" class="pa-2">
      <v-card-text class="white--text mt-1">
        <h1>Welcome back, mneelansh! 🎉</h1>

        <div class="mt-3">
          <router-link to="/account">Account settings</router-link>
        </div>
      </v-card-text>
    </v-card>

    <v-form @submit.prevent="" class="mt-5">
      <v-text-field type="text" v-model="search_term" placeholder="Search channels" solo></v-text-field>
    </v-form>

    <div class="mt-2">
      <h1>Recommended videos</h1>
      <v-row class="mt-5">
        <v-col cols="12" md="4" v-for="vid in vids" :key="vid.id">
          <v-card :to="'/play/' + vid.id">
            <v-img
              :aspect-ratio="16/9"
              :src="vid.thumbnail"
             />
            <v-card-title>{{ vid.title }}</v-card-title>
            <v-card-subtitle>{{ vid.description }}</v-card-subtitle>
          </v-card>
        </v-col>
      </v-row>
    </div>
  </v-container>
</template>

<script>

export default {
  name: "Dashboard",
  components: {},
  data: () => ({
    vids:[
      {
        id: 1,
        title: 'Video title',
        description: 'Video description',
        thumbnail: 'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80'
      },
      {
        id: 2,
        title: 'Video title',
        description: 'Video description',
        thumbnail: 'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80'
      },
      {
        id: 3,
        title: 'Video title',
        description: 'Video description',
        thumbnail: 'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80'
      },
      {
        id: 4,
        title: 'Video title',
        description: 'Video description',
        thumbnail: 'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80'
      },
      {
        id: 5,
        title: 'Video title',
        description: 'Video description',
        thumbnail: 'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80'
      },
      {
        id: 6,
        title: 'Video title',
        description: 'Video description',
        thumbnail: 'https://images.unsplash.com/photo-1616433784544-896eaf7b9e2a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1024&q=80'
      },
    ]
  })
};
</script>
