<template>
  <v-card
    class="mx-auto"
  >
    <div class="d-flex align-center justify-space-between">
      <div>
        <v-card-title v-text="title" class="mb-2">
        </v-card-title>
        <v-card-subtitle>
          <v-row>
            <v-col cols="12" md="auto" class="py-1 pr-0">
              <span class="mr-3">
                <v-icon class="mr-1">mdi-domain</v-icon>
                <span>{{ company.name }}</span>
              </span>
            </v-col>
            <v-col cols="12" md="auto" class="py-1 pr-0 pl-md-0">
              <span class="mr-3">
                <v-icon class="mr-1">mdi-map-marker</v-icon>
                <span>{{ location }}</span>
              </span>
            </v-col>
            <v-col cols="12" md="auto" class="py-1 pr-0 pl-md-0">
              <v-icon class="mr-1">mdi-cash-multiple</v-icon>
              <span class="font-weight-bold green--text darken-3">{{ payRange }}</span>
            </v-col>
          </v-row>
        </v-card-subtitle>
      </div>
      <div>
        <v-avatar size="64px" class="mx-4">
          <v-icon large>mdi-camera</v-icon>
        </v-avatar>
      </div>
    </div>
  </v-card>

</template>

<script>
    export default {
        name: "Announcement",
        props: {
            title: {
                type: String,
                required: true
            },
            company: {
                type: Object,
                required: true
            },
            paid: {
                type: Boolean,
                required: true
            },
            payRange: String,
            location: String
        }
    }
</script>

<style scoped>

</style>