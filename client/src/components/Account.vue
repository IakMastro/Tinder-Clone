<template>
  <div class="container">
    <hr>
    <user-details :user="this.$session.get('user')"></user-details>
    <div class="mt-3 mb-3 d-flex align-items-center justify-content-evenly">
      <button type="button" onclick="window.open('https://github.com/IakMastro/Tinder-Clone');"
              class="btn btn-secondary hide-text"
              role="button">
        <i class="bi bi-phone-fill"></i> Get the app <i class="bi bi-phone-fill"></i>
      </button>
    </div>
    <hr>
    <label>Upload Image for Profile
      <input type="file" id="file" ref="file" v-on:change="handleFileUpload">
    </label>

    <button class="btn btn-dark" v-on:click="submitFile">Submit</button>

    <hr>
    <alert :message="message" v-if="showMessage"></alert>
    <button type="button"
            class="btn btn-info btn-lg"
            v-b-modal:update-user-modal
            @click="getUserInfo">
      Update info
    </button>

    <b-modal ref="updateUserInfo"
             id="update-user-modal"
             title="Update user info"
             hide-footer>
      <b-form @submit="updateUser" @reset="resetUpdateForm" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="userForm.name"
                        required
                        placeholder="Enter name"/>
        </b-form-group>
        <b-form-group id="form-surname-group"
                      label="Surname:"
                      label-for="form-surname-input">
          <b-form-input id="form-surname-input"
                        type="text"
                        v-model="userForm.surname"
                        required
                        placeholder="Enter surname"/>
        </b-form-group>
        <b-form-group id="form-birthday-group"
                      label="Birthday:"
                      label-for="form-birthday-input">
          <b-form-input id="form-birthday-input"
                        type="date"
                        v-model="userForm.birthday"
                        required/>
        </b-form-group>
        <b-form-group id="form-gender-group"
                      label="Gender:"
                      label-for="form-gender-input">
          <select id="form-gender-input" v-model="userForm.gender">
            <option disabled value="">Please select your gender</option>
            <option>Male</option>
            <option>Female</option>
          </select>
        </b-form-group>
        <b-form-group id="form-weight-group"
                      label="Weight:"
                      label-for="form-weight-input">
          <b-form-input id="form-weight-input"
                        type="number"
                        v-model="userForm.weight"
                        required/>
        </b-form-group>
        <b-form-group id="form-height-group"
                      label="Height:"
                      label-for="form-height-input">
          <b-form-input id="form-height-input"
                        type="text"
                        v-model="userForm.height"
                        required/>
        </b-form-group>
        <b-form-group id="form-hair-group"
                      label="Hair Colour:"
                      label-for="form-hair-input">
          <select id="form-hair-input" v-model="userForm.hair_colour">
            <option disabled value="">Please select your gender</option>
            <option>Dark</option>
            <option>Blonde</option>
            <option>Ginger</option>
          </select>
        </b-form-group>
        <b-form-group id="form-eye-group"
                      label="Eye Colour:"
                      label-for="form-eye-input">
          <select id="form-eye-input" v-model="userForm.eye_colour">
            <option disabled value="">Please select your gender</option>
            <option>Blue</option>
            <option>Brown</option>
            <option>Green</option>
          </select>
        </b-form-group>
        <b-form-group id="form-bio-group"
                      label="Bio:"
                      label-for="form-bio-input">
          <b-form-textarea id="form-bio-input" v-model="userForm.bio"></b-form-textarea>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit Changes</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
import UserDetails from "@/components/UserDetails";
import Alert from '@/components/Alert.vue'
import Photo from '@/components/Photo.vue'

export default {
  name: "Account",
  data() {
    return {
      message: '',
      userForm: {},
      showMessage: false,
      path: `http://localhost:5000/user/${this.$session.get('user')['_id']}`,
      file: ''
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

  methods: {
    updateUser(evt) {
      evt.preventDefault()
      this.$refs.updateUserInfo.hide()

      const payload = {
        name: this.userForm.name,
        surname: this.userForm.surname,
        birthday: this.userForm.birthday,
        gender: this.userForm.gender,
        weight: this.userForm.weight,
        height: this.userForm.height,
        hair_colour: this.userForm.hair_colour,
        eye_colour: this.userForm.eye_colour,
        bio: this.userForm.bio
      }

      axios.put(this.path, payload).then((res) => {
        this.getUserInfo()
        this.message = res.data.message
        this.showMessage = true
      }).catch((error) => {
        console.error(error)
      })
    },

    resetUpdateForm(evt) {
      evt.preventDefault()
      this.userForm = this.$session.get('user')
    },

    getUserInfo() {
      axios.get(this.path).then((res) => {
        this.$session.set('user', res.data.user)
      })

      this.userForm = this.$session.get('user')
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0]
    },

    submitFile() {
      let formData = new FormData()
      formData.append('photo', this.file)
      formData.append('user', this.$session.get('user')['username'])
      const path = `http://localhost:5000/img/${this.file.name}`
      console.log(path)
      axios.post(path, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(() => console.log("EZ")).catch((error) => console.error(error))
      window.location.replace("settings?uploaded=1");
    }
  },

  created() {
    this.getUserInfo()
    if (this.$route.query.uploaded == 1) {
      setTimeout(function () {
        window.location.replace("settings");
      }, 3000);
    }
    if (this.$route.query.primePaid == 1) {
      setTimeout(function () {
        window.location.replace("settings");
      }, 100);
    }
  }
}
</script>