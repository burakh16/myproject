<template>
  <v-card color="blue-grey lighten-1">
    <v-row justify="center">
      <v-col cols="10" class="text-center pb-0">
        <h3>Join Now!</h3>
      </v-col>
      <v-col cols="10">
        <v-divider color="black"></v-divider>
      </v-col>
      <v-col cols="10" class="py-0">
        <v-text-field
          solo
          placeholder="Organization Name"
          label="Organization Name"
          class="mt-2"
          v-model="organization.organization"
        ></v-text-field>
      </v-col>
      <v-col cols="10" class="py-0">
        <v-text-field
          solo
          placeholder="Username"
          label="Username"
          class="mt-2"
          v-model="organization.username"
        ></v-text-field>
      </v-col>
      <v-col cols="10" class="py-0">
        <v-text-field
          solo
          placeholder="Name"
          label="Name"
          class="mt-2"
          v-model="organization.name"
        ></v-text-field>
      </v-col>
      <v-col cols="10" class="py-0">
        <v-text-field
          solo
          placeholder="Email"
          label="Email"
          type="email"
          class="mt-2"
          v-model="organization.email"
        ></v-text-field>
      </v-col>
      <v-col cols="10" class="py-0">
        <v-text-field
          solo
          placeholder="Password"
          label="Password"
          type="password"
          class="mt-2"
          v-model="organization.password"
        ></v-text-field>
      </v-col>
      <v-col cols="10" class="py-0">
        <v-btn color="primary" class="float-right mb-5" @click="save()"
          >Save</v-btn
        >
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data: () => ({
    organization: {
      organization: "",
      username: "",
      name: "",
      email: "",
      password: "",
    },
  }),
  methods: {
    ...mapActions(["createOrganization"]),
    async save() {
      await this.createOrganization(this.organization);
    },
  },
};
</script>

<style>
</style>