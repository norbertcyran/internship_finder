<template>
  <v-card
    class="mx-auto"
  >
    <VAnnouncementHeader
      :to="getDetailURL"
      :id="id"
      :location="location"
      :company="company"
      :paid="paid"
      :pay-range-bottom="payRangeBottom"
      :pay-range-top="payRangeTop"
      :title="title"
    ></VAnnouncementHeader>
  </v-card>

</template>

<script>
    import VAnnouncementHeader from "@/components/VAnnouncementHeader";
    export default {
        name: "AnnouncementListItem",
        components: {VAnnouncementHeader},
        props: {
            id: {
                type: Number,
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
            getDetailURL() {
                return `/announcements/${this.id}`
            }
        }
    }
</script>

<style scoped>

</style>