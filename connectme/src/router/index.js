import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Data from "../views/Data.vue";
import Team from "../views/Team.vue";
import AboutInfo from "../views/AboutInfo.vue";
import Documentation from "../views/Documentation.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    children: [
      {
        path: "/about",
        name: "About",
        component: AboutInfo,
      }
    ]
  },
  {
    path: "/home",
    name: "Home",
    component: Home
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
  },
  {
    path: "/documentation",
    name: "Documentation",
    component: Documentation
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
