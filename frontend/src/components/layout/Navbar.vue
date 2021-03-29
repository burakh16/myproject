<template>
  <q-header reveal bordered class="bg-primary text-white q-px-sm">
    <q-toolbar>
      <q-btn dense flat round icon="menu" @click="left = !left" />

      <q-toolbar-title>
        <q-avatar>
          <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg" />
        </q-avatar>
        Title
      </q-toolbar-title>

      <q-btn dense flat icon="login" class="q-mr-md" :to="{ name: 'Login' }"
        >Login</q-btn
      >
      <q-btn dense flat icon="login" class="q-mr-md" :to="{ name: 'About' }"
        >About</q-btn
      >

      <q-btn round dense flat icon="language">
        <q-menu>
          <q-list>
            <q-item
              clickable
              v-close-popup
              v-for="entry in languages"
              :key="entry.title"
              @click="changeLocale(entry.language)"
            >
              <q-item-section
                ><flag :iso="entry.flag" v-bind:squared="false"
              /></q-item-section>
            </q-item>
          </q-list>
        </q-menu>
      </q-btn>
    </q-toolbar>
  </q-header>
</template>

<script>
import i18n from "@/plugins/i18n";

export default {
  data() {
    return {
      left: false,
      languages: [
        { flag: "us", language: "en" },
        { flag: "tr", language: "tr" },
      ],
    };
  },
  methods: {
    changeLocale(locale) {
      i18n.locale = locale;
    },
  },
};
</script>

<style>
</style>