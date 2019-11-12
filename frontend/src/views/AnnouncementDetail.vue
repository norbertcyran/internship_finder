<template>
  <v-container>
    <v-row>
      <v-col
        md="8"
        cols="12"
      >
        <v-card>
          PLACEHOLDER
        </v-card>
      </v-col>
      <v-col
        md="4"
        cols="12"
      >
        <v-card>
          <v-card-title class="pb-0 headline font-weight-light">Apply for the internship</v-card-title>
          <v-card-text>
            <AnnouncementApplyForm class="px-2"></AnnouncementApplyForm>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
    import AnnouncementApplyForm from "@/components/AnnouncementApplyForm";
    export default {
        name: "AnnouncementDetail",
        components: {AnnouncementApplyForm}
    }
</script>

<style scoped>

</style>