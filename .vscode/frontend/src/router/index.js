import Vue from "vue";
import VueRouter from "vue-router";
import stats from "../components/stats.vue";
import comparing from "../components/comparing.vue";
import home from "../components/home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/nba",
    name: "stats",
    component: stats,
  },
  {
    path: "/",
    name: "home",
    component: home,
  },
  {
    path: "/comparing",
    name: comparing,
    component: comparing,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
