<template>
  <v-row justify="center" class="mt-3">
    <v-col cols="7">
      <new-organization />
    </v-col>
  </v-row>
</template>

<script>
import NewOrganization from "../components/organizations/NewOrganization.vue";
export default {
  components: {
    NewOrganization,
  },
};
</script>

<style></style>
