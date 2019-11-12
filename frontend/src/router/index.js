import VueRouter from "vue-router";
import Announcements from "@/views/Announcements";
import Login from "@/views/Login";
import store from "@/store";
import AnnouncementDetail from "@/views/AnnouncementDetail";


const ifNotAuthenticated = (to, from, next) => {
    if (!store.getters.isAuthenticated)
        next();
    else
        next(false);
};

const routes = [
    { path: '/', component: Announcements },
    { path: '/announcements', component: Announcements },
    { path: '/announcements/:announcement_id', component: AnnouncementDetail, prop: true },
    { path: '/login', component: Login, beforeEnter: ifNotAuthenticated },
    { path: '*', redirect: '/'}
];


export default new VueRouter({ routes });