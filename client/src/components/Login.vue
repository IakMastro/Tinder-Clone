<template>
  <div class="container">
    <alert :message="message" v-if="showMessage"></alert>
    <h5>Welcome back!</h5>

    <div class="d-flex flex-column justify-content-center align-items-center container p-5 shadow"
         style="color: white; background-color: #303030; border-radius: 20px; width: 40%;">

      <div class="mb-4 form-floating">
        <input type="email" class="form-control" id="email" name="email" placeholder=" ">
        <label for="email" style="color: rgba(0, 0, 0, 0.5);">Email</label>
      </div>
      <div class="mb-3 form-floating">
        <input type="password" class="form-control" id="pwd" name="pwd" placeholder=" ">
        <label for="pwd" style="color: rgba(0, 0, 0, 0.5);">Password</label>
      </div>


      <button type="submit"
              class="btn btn-primary"
              @click="onLogin">
        Log In
      </button>
    </div>
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
          <b-form-group id="form-gender-group"
                        label="Gender:"
                        label-for="form-gender-input">
            <select id="form-gender-input" v-model="registerForm.gender">
              <option disabled value="">Please select your gender</option>
              <option>Male</option>
              <option>Female</option>
              <!--            <option>Other</option>-->
            </select>
          </b-form-group>
          <b-form-group id="form-weight-group"
                        label="Weight:"
                        label-for="form-weight-input">
            <b-form-input id="form-weight-input"
                          type="number"
                          v-model="registerForm.weight"
                          required/>
          </b-form-group>
          <b-form-group id="form-height-group"
                        label="Height:"
                        label-for="form-height-input">
            <b-form-input id="form-height-input"
                          type="text"
                          v-model="registerForm.height"
                          required/>
          </b-form-group>
          <b-form-group id="form-hair-group"
                        label="Hair Colour:"
                        label-for="form-hair-input">
            <select id="form-hair-input" v-model="registerForm.hair_colour">
              <option disabled value="">Please select your gender</option>
              <option>Dark</option>
              <option>Blonde</option>
              <option>Ginger</option>
            </select>
          </b-form-group>
          <b-form-group id="form-eye-group"
                        label="Eye Colour:"
                        label-for="form-eye-input">
            <select id="form-eye-input" v-model="registerForm.eye_colour">
              <option disabled value="">Please select your gender</option>
              <option>Blue</option>
              <option>Brown</option>
              <option>Green</option>
            </select>
          </b-form-group>
          <b-form-group id="form-bio-group"
                        label="Bio:"
                        label-for="form-bio-input">
            <b-form-textarea id="form-bio-input" v-model="registerForm.bio"></b-form-textarea>
          </b-form-group>
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
import {calculate_age} from "@/ts/lib";

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
              this.$router.push('/settings')
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

      if (calculate_age(new Date(this.registerForm.birthday)) > 17 &&
          this.registerForm.password === this.registerForm.repeatPwd) {
        const payload = {
          email: this.registerForm.email,
          username: this.registerForm.email.split("@")[0],
          name: this.registerForm.name,
          surname: this.registerForm.surname,
          password: this.registerForm.password,
          birthday: this.registerForm.birthday,
          gender: this.registerForm.gender,
          weight: this.registerForm.weight,
          height: this.registerForm.height,
          hair_colour: this.registerForm.hair_colour,
          eye_colour: this.registerForm.eye_colour,
          bio: this.registerForm.bio
        }

        this.signup(payload)
      } else if (this.registerForm.password !== this.registerForm.repeatPwd) {
        this.message = 'Passwords must match'
        this.showMessage = true
      } else {
        this.message = 'You must be over 18 to register'
        this.showMessage = true
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
