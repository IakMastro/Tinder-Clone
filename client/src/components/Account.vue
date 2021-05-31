<template>
  <div class="container">

    <hr>
    <user-details :user="this.$session.get('user')"></user-details>

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
            <option>Other</option>
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
          <b-form-input id="form-hair-input"
                        type="text"
                        v-model="userForm.hair_colour"
                        required
                        placeholder="Enter your hair colour"/>
        </b-form-group>
        <b-form-group id="form-eye-group"
                      label="Eye Colour:"
                      label-for="form-eye-input">
          <b-form-input id="form-eye-input"
                        type="text"
                        v-model="userForm.eye_colour"
                        required
                        placeholder="Enter your eye colour"/>
        </b-form-group>
        <b-form-group id="form-sexual-group"
                      label="Sexual Orientation:"
                      label-for="form-sexual-input">
          <select v-model="userForm.sexual_orientation">
            <option disabled value="">Please select your sexual orientation</option>
            <option>Heterosexual</option>
            <option>Homosexual</option>
            <option>Bisexual</option>
            <option>Asexual</option>
            <option>Other</option>
          </select>
        </b-form-group>
        <b-form-group id="form-education-group"
                      label="Education:"
                      label-for="form-education-input">
          <select v-model="userForm.education">
            <option disabled value="">Please select your education</option>
            <option>University</option>
            <option>Senior High School</option>
            <option>Junior High School</option>
            <option>Primary School</option>
          </select>
        </b-form-group>
        <b-form-group id="form-checkbox-group"
                      label="Do you...?"
                      label-for="form-checkbox-input">
          <input type="checkbox"
                 v-model="userForm.smoker"
                 true-value="true"
                 false-value="false">
          &nbsp;<span>smoke?</span><br>
          <input type="checkbox"
                 v-model="userForm.drinker"
                 true-value="true"
                 false-value="false">
          &nbsp;<span>drink?</span><br>
          <input type="checkbox"
                 v-model="userForm.children"
                 true-value="true"
                 false-value="false">
          &nbsp;<span>have children?</span><br>
        </b-form-group>
        <b-form-group id="form-status-group"
                      label="Status:"
                      label-for="form-status-input">
          <b-form-input id="form-status-input"
                        type="text"
                        v-model="userForm.status"
                        required
                        placeholder="Enter status"/>
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
        sexual_orientation: this.userForm.sexual_orientation,
        education: this.userForm.education,
        smoker: this.userForm.smoker,
        drinker: this.userForm.drinker,
        children: this.userForm.children,
        status: this.userForm.status
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
      }).then(() => console.log("Success!")).catch((error) => console.error(error))
    }
  },

  created() {
    this.getUserInfo()
  }
}
</script>