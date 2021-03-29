<template>
  <div>
    <component :is="this.$route.meta.layout || 'Default'">
      <router-view />
    </component>
  </div>
</template>

<script>
import Default from "@/layouts/Default.vue";
import Main from "@/layouts/Main.vue";

export default {
  name: "App",

  methods: {},
  created() {},
  components: {
    Default,
    Main,
  },
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.2s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0;
}

.content {
  white-space: pre-wrap;
  word-wrap: break-word;
  font-family: inherit;
}
</style>
