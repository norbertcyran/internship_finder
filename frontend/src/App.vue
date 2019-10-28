<template>
  <v-app>
    <v-app-bar
            app
            color="blue darken-3"
            dark
            clipped-left
    >
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-light">INTERNSHIP FINDER</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text>Sign up</v-btn>
      <v-btn text class="mr-3">Log in</v-btn>
      <v-avatar size="32px">
        <v-img :src="require('./assets/logo.svg')"></v-img>
      </v-avatar>
    </v-app-bar>

    <v-content>
        <Announcements/>
    </v-content>
  </v-app>
</template>

<script>
import Announcements from "./components/Announcements";

export default {
  name: 'App',
  components: {
    Announcements
  },
  data: () => ({
    //
  }),
};
</script>
