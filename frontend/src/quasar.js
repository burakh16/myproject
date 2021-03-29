import Vue from "vue";

import "./styles/quasar.sass";
import "@quasar/extras/material-icons/material-icons.css";
import { Quasar, Notify } from "quasar";

Vue.use(Quasar, {
  config: {},
  plugins: { Notify},
});
