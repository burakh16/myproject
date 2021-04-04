<template>
  <div class="row full-height" id="home">
    <div class="col-md-6 q-mt-xl">
      <strong class="q-px-xl"
        >Please enter your organization name to start free trial.</strong
      >
      <q-input
        outlined
        dense
        v-model="text"
        label="Enter organization name..."
        class="q-px-xl q-mt-md"
      >
        <template v-slot:after>
          <q-btn color="primary" label="Start" />
        </template>
      </q-input>
    </div>
    <div class="col-md-6 q-mt-xl">
      <h3 class="q-my-xs">Welcome to MyProject HomePage</h3>
    </div>
    <!--   <p>{{ $t("test") }}</p> -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: "Home",
  components: {},
  data() {
    return {
      text: "",
    };
  },
};
</script>

<style>
</style>