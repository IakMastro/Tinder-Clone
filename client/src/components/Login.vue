<template>
  <div class="container">
    <alert :message="message" v-if="showMessage"></alert>
    <h5>Welcome back!</h5>

    <div class="form-group">
      <label for="email">Email:</label>
      <input type="email" class="form-control" id="email" placeholder="Enter email" name="email">
    </div>

    <div class="form-group">
      <label for="pwd">Password:</label>
      <input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pwd">
    </div>

    <button type="submit"
            class="btn btn-primary"
            @click="onLogin">
      Log In
    </button>

    <hr>
    <h5>New here?</h5>
    <button type="button"
            class="btn btn-primary"
            v-b-modal.register-modal>
      Sign Up
    </button>

    <b-modal ref="registerModal"
             id="register-modal"
             title="Enter your credentials"
             hide-footer>
      <b-form @submit="onSignUp" @reset="resetRegisterForm" class="w-100">
        <b-form-group id="form-email-group"
                      label="Email:"
                      label-for="form-email-input">
          <b-form-input id="form-email-input"
                        type="email"
                        v-model="registerForm.email"
                        required
                        placeholder="Enter your email">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-group">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="registerForm.name"
                        required
                        placeholder="Enter your name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-surname-group"
                      label="Surname:"
                      label-for="form-surname-group">
          <b-form-input id="form-surname-input"
                        type="text"
                        v-model="registerForm.surname"
                        required
                        placeholder="Enter your surname">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-group"
                      label="Password:"
                      label-for="form-password-input">
          <b-form-input id="form-password-input"
                        type="password"
                        v-model="registerForm.password"
                        required
                        placeholder="Enter password">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-repeatPwd-group"
                      label="Repeat password:"
                      label-for="form-repeatPwd-input">
          <b-form-input id="form-repeatPwd-input"
                        type="password"
                        v-model="registerForm.repeatPwd"
                        required
                        placeholder="Enter password again">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-birthday-group"
                      label="Birthday:"
                      label-for="form-birthday-input">
          <b-form-input id="form-birthday-input"
                        type="date"
                        v-model="registerForm.birthday"
                        required>
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from './Alert.vue'
import $ from 'jquery'

export default {
  name: 'Login',
  data() {
    return {
      user: [],
      registerForm: {
        email: '',
        name: '',
        surname: '',
        password: '',
        repeatPwd: '',
        birthday: '',
      },
      message: '',
      showMessage: false,
      path: 'http://localhost:5000',
    }
  },

  components: {
    Alert,
  },

  beforeCreate() {
    if (this.$session.exists())
      this.$router.push('/')
  },

  methods: {
    onLogin() {
      const payload = {
        email: $('#email').val(),
        password: $('#pwd').val(),
      }

      this.login(payload)
    },

    login(payload) {
      const path = this.path.concat(`/login`)
      axios.put(path, payload)
          .then((res) => {
            this.user = res.data.user
            this.message = res.data.message
            this.showMessage = true

            if (this.user !== undefined) {
              this.$session.start()
              this.$session.set('user', this.user)
              this.$router.push('/')
            }
          })
          .catch((error) => {
            console.error(error)
          });
    },

    initForm() {
      this.registerForm.username = ''
      this.registerForm.password = ''
      this.registerForm.repeatPwd = ''
      this.user = []
      this.message = ''
      this.showMessage = false
    },

    resetRegisterForm() {
      this.registerForm.username = ''
      this.registerForm.password = ''
      this.registerForm.repeatPwd = ''
    },

    onSignUp(evt) {
      evt.preventDefault()
      this.$refs.registerModal.hide()

      if (this.registerForm.password === this.registerForm.repeatPwd) {
        const payload = {
          email: this.registerForm.email,
          username: this.registerForm.email.split("@")[0],
          name: this.registerForm.name,
          surname: this.registerForm.surname,
          password: this.registerForm.password,
          birthday: this.registerForm.birthday
        }

        this.signup(payload)
      } else {
        this.message = 'Passwords must match'
      }
    },

    signup(payload) {
      const path = this.path.concat('/register')
      axios.post(path, payload)
          .then((res) => {
            this.message = res.data.message
            this.resetRegisterForm()
            this.showMessage = true
          })
    },
  },
};
</script>

<style scoped>

</style>
