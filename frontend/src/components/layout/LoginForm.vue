<template>
  <q-form @submit="onSubmit" class="q-gutter-md q-mt-xl">
    <q-input
      outlined
      dense
      v-model="user.username"
      label="Your name *"
      hint="Name and surname"
      lazy-rules
      :rules="usernameValidations"
    />

    <q-input
      v-model="user.password"
      outlined
      dense
      :type="isPwd ? 'password' : 'text'"
      hint="Password with toggle"
    >
      <template v-slot:append>
        <q-icon
          :name="isPwd ? 'visibility_off' : 'visibility'"
          class="cursor-pointer"
          @click="isPwd = !isPwd"
        />
      </template>
    </q-input>

    <div>
      <q-btn label="Submit" type="submit" color="primary" />
    </div>
  </q-form>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      user: {
        username: "",
        password: "",
      },
      isPwd: true,
    };
  },
  computed: {
    usernameValidations() {
      return [(val) => (val && val.length > 0) || "Please type something"];
    },
  },
  methods: {
    ...mapActions(["login"]),
    async onSubmit(e) {
        e.preventDefault();
      await this.login(this.user);
      this.$q.notify({
        color: "red-5",
        textColor: "white",
        icon: "warning",
        message: "You need to accept the license and terms first",
      });
      /*  this.$q.notify({
        color: "green-4",
        textColor: "white",
        icon: "cloud_done",
        message: "Submitted",
        position: "top-right",
      }); */
    },
  },
};
</script>

<style>
</style>