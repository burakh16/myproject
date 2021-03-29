<template>
  <div class="home">
    <p>{{ $t("test") }}</p>
    <p>testtt</p>
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
