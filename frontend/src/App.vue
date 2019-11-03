<template>
  <v-app>
    <v-app-bar
            app
            color="blue darken-3"
            dark
            clipped-left
    >
      <v-toolbar-title class="headline text-uppercase">
        <router-link
          to="/"
          exact
          class="font-weight-light"
          tag="span"
          style="cursor: pointer;"
        >INTERNSHIP FINDER</router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="mr-1" text>Sign up</v-btn>
      <v-btn text class="mr-3" to="/login" exact>Log in</v-btn>
      <v-avatar size="32px">
        <v-img :src="require('./assets/logo.svg')"></v-img>
      </v-avatar>
    </v-app-bar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
    //
  }),
};
</script>
