<template>
  <v-app>
    <navbar />
    <v-main  class="app">
      <div class="container">
        <router-view />
      </div>
    </v-main>
  </v-app>
</template>

<script>
import navbar from "@/components/Navbar";

export default {
  name: "App",

  data: () => ({
    //
  }),
  components: {
    navbar,
  },
};
</script>

<style>
.app {
  background-color: #CFD8DC;
}
</style>
