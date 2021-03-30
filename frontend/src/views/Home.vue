<template>
  <div class="home">
    <p>{{ $t("test") }}</p>
   <h1>test</h1>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "Home",
  components: {},
  data() {
    return {};
  },
};
</script>
