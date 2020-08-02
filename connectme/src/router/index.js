import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Data from "../views/Data.vue";
import Team from "../views/Team.vue";
import Instructions from "../views/Instructions.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    children: [
      {
        path: "/instructions",
        name: "Instructions",
        component: Instructions,
      }
    ]
  },
  {
    path: "/home",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    component: About
  },
  {
    path: "/data",
    name: "Data",
    component: Data
  },
  {
    path: "/team",
    name: "Team",
    component: Team
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
