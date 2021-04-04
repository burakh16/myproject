import Vue from "vue";
import Vuex from "vuex";
import users from './modules/users'
import core from './modules/core'
import organizations from './modules/organizations'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: { users, core, organizations },
});
