import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      layout: "Main"
    }
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import("../views/About.vue"),
  },
  {
    path: "/organizations/new",
    name: "NewOrganizations",
    component: () =>
      import("../views/NewOrganization.vue"),
    meta: {
      layout: "Main"
    }
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import("../views/Default/Login.vue"),
    meta: {
      layout: "Main"
    }
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
