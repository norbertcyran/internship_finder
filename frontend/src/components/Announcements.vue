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
                <Announcement
                  v-bind="announcement"
                ></Announcement>
           </v-col>
       </v-row>
   </v-container>
</template>

<script>
    import Announcement from "./Announcement";
    export default {
        name: "Announcements",
        components: {Announcement},
        data() {
            return {
                announcements: [
                    {
                        id: 1,
                        title: "Python Trainee",
                        company: {
                            name: 'Nokmarch'
                        },
                        paid: true,
                        location: "Janiszewskiego, Wrocław",
                        payRange: "300 - 420 PLN"
                    },
                    {
                        id: 2,
                        title: "Senior Cobol Intern",
                        company: {
                            name: "Grand Bank GMBH"
                        },
                        paid: true,
                        location: "Sienkiewicza 28/30, Wrocław",
                        payRange: "100 - 150 PLN"
                    }
                ]
            }
        }
    }
</script>

<style scoped>

</style>