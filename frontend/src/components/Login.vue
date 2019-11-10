<template>
  <v-container class="fill-height">
    <v-row align-content="center" justify="center">
      <v-col cols="10" sm="6" md="4">
        <v-form ref="form" @submit.prevent="handleSubmit">
          <v-row>
            <v-col class="text-center">
              <h3 class="display-1 font-weight-light">Log in</h3>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="password"
                label="Password"
                type="password"
                :rules="[v => !!v || 'Password is required']"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row justify="end">
            <v-col cols="auto">
              <v-btn type="submit" color="primary">Login</v-btn>
            </v-col>
          </v-row>
          <v-row v-show="this.authStatus === 'failure'">
            <v-col>
              <v-alert
                type="error"
                dense
                outlined
              >{{ this.authError }}</v-alert>
            </v-col>
          </v-row>
          <v-row class="text-center">
            <v-col>
              Forgot your password? <router-link to="/forgot-password">Click here</router-link>.
            </v-col>
          </v-row>
          <v-row class="text-center">
            <v-col>
              Do not have an account? <router-link to="/register">Register</router-link>.
            </v-col>
          </v-row>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
    import { mapActions, mapState } from 'vuex';
    import { LOGIN } from "../store/action-types";

    export default {
        name: "login",
        data() {
            return {
                email: "",
                password: "",
                emailRules: [
                    v => !!v || "E-mail is required",
                    v => /.+@.+\..+/.test(v) || "E-mail is not valid."
                ],
            }
        },
        computed: {
            ...mapState({
                authStatus: state => state.auth.status,
                authError: state => state.auth.error
            })
        },
        methods: {
            ...mapActions({
                login: LOGIN
            }),
            async handleSubmit() {
                if (this.validate()) {
                    await this.login({email: this.email, password: this.password});
                    if (this.authStatus === 'success') {
                        await this.$router.push('/');
                    }
                }
            },
            validate() {
                return this.$refs.form.validate()
            }
        }
    }
</script>

<style scoped>

</style>