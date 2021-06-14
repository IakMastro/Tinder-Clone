<template>
  <div class="container">
    <hr>
    <div class="mt-3 mb-3 d-flex align-items-center justify-content-evenly">
      <button type="button" @click=""
              class="btn btn-danger hide-text"
              role="button">
        <i class="bi bi-heart-fill"></i>
      </button>

      <button type="button"
              class="btn btn-primary hide-text"
              role="button"
              v-b-modal.contact-modal>
        <i class="bi bi-envelope-fill"></i>
      </button>
    </div>
    <user-details :user="user"></user-details>

    <b-modal ref="contactModal"
             id="contact-modal"
             title="Enter your message"
             centered>
      <b-form @submit="contact" class="w-100">
        <b-form-group id="form-logged-in-group"
                      label="From:"
                      label-for="form-logged-in-input">
          <b-form-input id="form-logged-in-input"
                        type="email"
                        v-model="contactForm.signed_in"
                        required
                        readonly>
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-to-send-group"
                      label="To:"
                      label-for="form-to-send-input">
          <b-form-input id="form-to-send-group"
                        type="email"
                        v-model="contactForm.to_sent"
                        required
                        readonly>
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-bio-group"
                      label="Message:"
                      label-for="form-bio-input">
          <b-form-textarea id="form-bio-input"
                           v-model="contactForm.message"
                           placeholder="Enter your message"></b-form-textarea>
        </b-form-group>
      </b-form>

    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import UserDetails from "@/components/UserDetails";
import Alert from '@/components/Alert.vue'

export default {
  name: "Profile",

  data() {
    return {
      contactForm: {},
      path: 'http://localhost:5000/user/',
    }
  },

  components: {
    Alert,
    UserDetails,
  },

  beforeCreate() {
    if (!this.$session.exists())
      this.$router.push('/login')
  },

  props: ['user'],

  methods: {
    contact() {
      this.$router.push(`/contact/${this.user._id}`)
    },

    getUserInfo() {
      axios.get(this.path.concat(this.$route.params.id)).then((res) => {
        this.user = res.data.user
        this.contactForm.to_sent = this.user.email
        this.contactForm.signed_in = this.$session.get('user').email
      })
    }
  },

  created() {
    this.getUserInfo()
  }
}
</script>