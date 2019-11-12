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
      <template v-if="!isAuthenticated" >
        <v-btn class="mr-1" text>Sign up</v-btn>
        <v-btn text to="/login" exact>Login</v-btn>
      </template>
      <template v-else>
        <v-btn text class="mr-3" @click="logout">Logout</v-btn>
        <v-avatar size="32px">
          <v-img :src="require('./assets/logo.svg')"></v-img>
        </v-avatar>
      </template>
    </v-app-bar>
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import { LOGOUT } from "./store/action-types";
export default {
  name: 'App',
  data: () => ({
    //
  }),
  computed: {
      ...mapGetters([
          'isAuthenticated'
      ])
  },
  methods: {
      ...mapActions({
          logout: LOGOUT
      })
  }
};
</script>

<style>
  a {
    text-decoration: none;
  }
</style>
