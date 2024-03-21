// DEFINE OUR ROUTING RULES //

import {createRouter,createWebHistory} from "vue-router"
import HomeView from "../views/HomeView.vue"
import AboutView from "../views/AboutView.vue"
import Monitor from "@/views/Monitor.vue"
import History from "@/views/History.vue"
const router = createRouter({
    history : createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path:"/",
            name : "monitor",
            component: Monitor
        },
        {
            path:"/about",
            name : "about",
            component: AboutView
        },
        {
            path:"/history",
            name : "history",
            component: History
        },
    ]
})
export default router