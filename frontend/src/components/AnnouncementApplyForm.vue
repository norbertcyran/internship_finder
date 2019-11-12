<template>
  <v-form>
    <v-row>
      <v-col>
        <v-text-field
          label="Name"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          label="E-mail"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-file-input
          label="CV"
        ></v-file-input>
      </v-col>
    </v-row>
    <v-row justify="end">
      <v-col cols="auto">
        <v-btn color="primary">Apply</v-btn>
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
    export default {
        name: "AnnouncementApplyForm"
    }
</script>

<style scoped>

</style>