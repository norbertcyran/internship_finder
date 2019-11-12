<template>
   <v-container>
       <v-row
         v-for="announcement in announcements"
         :key="announcement.id"
         align="center"
       >
           <v-col
             cols="12"
             class="py-1"
           >
                <VAnnouncement
                  :id="announcement.id"
                  :title="announcement.title"
                  :company="announcement.company"
                  :location="announcement.location"
                  :paid="announcement.paid"
                  :pay-range-bottom="announcement.pay_range_bottom"
                  :pay-range-top="announcement.pay_range_top"
                ></VAnnouncement>
           </v-col>
       </v-row>
   </v-container>
</template>

<script>
    import VAnnouncement from "../components/VAnnouncement";
    import {mapState} from "vuex";
    import {GET_ANNOUNCEMENTS} from "@/store/action-types";
    export default {
        name: "Announcements",
        components: {
            VAnnouncement
        },
        computed: {
            ...mapState({
                announcements: state => state.announcements.announcements
            })
        },
        created() {
            this.$store.dispatch(GET_ANNOUNCEMENTS);
        }
    }
</script>

<style scoped>

</style>