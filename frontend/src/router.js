import VueRouter from "vue-router";
import Announcements from "./components/Announcements";
import Login from "./components/Login";


const routes = [
    { path: '/', component: Announcements },
    { path: '/announcements', component: Announcements },
    { path: '/login', component: Login },
    { path: '*', redirect: '/'}
];


export default new VueRouter({ routes });