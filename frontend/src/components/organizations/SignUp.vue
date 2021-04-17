<template>
  <div class="row justify-center">
    <div class="col-12 col-md-8 col-lg-6">
      <q-card class="my-card">
        <q-card-section>
          <div class="text-h6">Create your MyProject account.</div>
        </q-card-section>

        <q-separator />

        <q-card-section>
          <q-form @submit="onSubmit">
            <div class="row">
              <div class="col-12">
                <q-input
                  outlined
                  dense
                  v-model="user.name"
                  label="Your name *"
                  lazy-rules
                  :rules="usernameValidations"
                />
              </div>
              <div class="col-12">
                <q-input
                  outlined
                  dense
                  v-model="user.username"
                  label="Username *"
                  lazy-rules
                  :rules="usernameValidations"
                />
              </div>
              <div class="col-12">
                <q-input
                  outlined
                  dense
                  v-model="user.email"
                  label="Email *"
                  lazy-rules
                  :rules="usernameValidations"
                />
              </div>
              <div class="col-12">
                <q-input
                  v-model="user.password"
                  outlined
                  label="Password *"
                  dense
                  hint="Your password must contains"
                  :type="isPwd ? 'password' : 'text'"
                >
                  <template v-slot:append>
                    <q-icon
                      :name="isPwd ? 'visibility_off' : 'visibility'"
                      class="cursor-pointer"
                      @click="isPwd = !isPwd"
                    />
                  </template>
                </q-input>
              </div>
              <div class="col-12 q-mt-xs">
                <q-btn
                  label="Submit"
                  type="submit"
                  color="primary"
                  class="float-right q-px-lg"
                />
              </div>
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      user: {
        username: "",
        name: "",
        email: "",
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
    ...mapActions(["createNewOrganization"]),
    async onSubmit(e) {
      try {
        e.preventDefault();
        await this.createNewOrganization(this.user);
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "You need to accept the license and terms first",
        });
      } catch (error) {
        this.$q.notify({
          color: "green-4",
          textColor: "white",
          icon: "cloud_done",
          message: "Submitted",
          position: "top-right",
        });
      }
    },
  },
};
</script>

<style>
</style>