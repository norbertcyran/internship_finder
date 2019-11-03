<template>
  <v-container class="fill-height">
    <v-row align-content="center" justify="center">
      <v-col cols="10" sm="6" md="4">
        <v-form>
          <v-row>
            <v-col class="text-center">
              <h3 class="display-1 font-weight-light">Log in</h3>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="E-mail"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                label="Password"
                type="password"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="auto">
              <v-btn color="primary">Log in</v-btn>
            </v-col>
          </v-row>
          <v-row class="text-center">
            <v-col>
              Forgot your password? <a href="">Click here</a>.
            </v-col>
          </v-row>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
    export default {
        name: "login"
    }
</script>

<style scoped>

</style>