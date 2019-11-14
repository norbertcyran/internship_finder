<template>
  <v-container>
    <v-row>
      <v-col
        md="8"
        cols="12"
      >
        <v-skeleton-loader
          type="article"
          v-if="announcementLoading"
        ></v-skeleton-loader>
        <v-card v-else-if="!!announcement">
          <VAnnouncementHeader
            :id="announcementId"
            :pay-range-top="announcement.pay_range_top"
            :pay-range-bottom="announcement.pay_range_bottom"
            :paid="announcement.paid"
            :title="announcement.title"
            :company="announcement.company"
            :location="announcement.location"
          ></VAnnouncementHeader>
          <v-divider></v-divider>
          <v-card-title class="font-weight-light">
            Description
          </v-card-title>
          <v-card-text>
              {{ announcement.description }}
          </v-card-text>
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
    import {mapGetters} from "vuex";
    import {GET_ANNOUNCEMENT} from "@/store/action-types";
    import VAnnouncementHeader from "@/components/VAnnouncementHeader";
    export default {
        name: "AnnouncementDetail",
        components: {VAnnouncementHeader, AnnouncementApplyForm},
        props: {
            announcementId: {
                type: [Number, String],
                required: true
            }
        },
        computed: {
            ...mapGetters([
                'announcement',
                'announcementLoading'
            ]),
            payRange() {
                return `${this.announcement.pay_range_bottom} - ${this.announcement.pay_range_top} PLN`
            }
        },
        watch: {
            announcementId: async function (val) {
                await this.$store.dispatch(GET_ANNOUNCEMENT, val)
            }
        },
        created() {
            this.$store.dispatch(GET_ANNOUNCEMENT, this.announcementId);
        }
    }
</script>

<style scoped>

</style>