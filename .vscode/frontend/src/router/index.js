import Vue from "vue";
import VueRouter from "vue-router";
import SharkE from "../components/SharkE.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/shark",
    name: "shark",
    component: SharkE,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
