import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth';
import announcements from "./modules/announcements";
import announcement from "@/store/modules/announcement";

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        auth,
        announcements,
        announcement
    }
});