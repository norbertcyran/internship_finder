<template>
  <div class="d-flex align-center justify-space-between">
    <div>
      <v-card-title class="mb-2">
        <router-link v-if="to" :to="to">{{ title }}</router-link>
        <template v-else>{{ title }}</template>
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
      <v-avatar size="80px" class="mx-4">
        <v-img v-if="company.logo" :src="company.logo"></v-img>
        <v-icon v-else large>mdi-camera</v-icon>
      </v-avatar>
    </div>
  </div>

</template>

<script>
    export default {
        name: "VAnnouncementHeader",
        props: {
            to: String,
            id: {
                type: [String, Number],
                required: true
            },
            title: {
                type: String,
                required: true
            },
            company: {
                type: Object,
                required: true,
            },
            paid: {
                type: Boolean,
                required: true
            },
            payRangeTop: Number,
            payRangeBottom: Number,
            location: String
        },
        computed: {
            payRange() {
                return `${this.payRangeBottom} - ${this.payRangeTop} PLN`
            },
        }

    }
</script>

<style scoped>

</style>