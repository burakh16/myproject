import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "./quasar";

import  i18n  from '@/plugins/i18n'
//import { Trans } from './plugins/Translation'

//Vue.prototype.$i18nRoute = Trans.i18nRoute.bind(Trans)

Vue.config.productionTip = false;


new Vue({
  router,
  store,
  i18n,
  render: (h) => h(App),
}).$mount("#app");
