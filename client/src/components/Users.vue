<template>
  <div class="container">
    <form style="width: 50%; margin-left: auto; margin-right: auto;" @submit="filterSearch"
          v-if="this.$session.get('user').type==='premium'">
      <div class="row mb-3">
        <div class="col-6">
          <label for="text_box_weight_minimum" class="form-label">Min weight (kg)</label>
          <input type="number" min="40" max="300" class="form-control" id="text_box_weight_minimum"
                 name="text_box_weight_minimum">
        </div>
        <div class="col-6">
          <label for="text_box_weight_maximum" class="form-label">Max weight (kg)</label>
          <input type="number" min="40" max="300" class="form-control" id="text_box_weight_maximum"
                 name="text_box_weight_maximum">
        </div>
      </div>
      <hr>
      <div class="row mb-3">
        <div class="col-6">

          <label for="text_box_height_minimum" class="form-label">Min Height (cm)</label>
          <input type="number" min="100" max="250" class="form-control" id="text_box_height_minimum"
                 name="text_box_height_minimum">
        </div>
        <div class="col-6">
          <label for="text_box_height_maximum" class="form-label">Max Height (cm)</label>
          <input type="number" min="100" max="250" class="form-control" id="text_box_height_maximum"
                 name="text_box_height_maximum">
        </div>
      </div>
      <hr>
      <div class="row mb-3">
        <div class="col-4 form-check">
          <input type="checkbox" class="form-check-input" id="blue_eye_checkbox" name="blue_eye_checkbox">
          <label class="form-check-label" for="blue_eye_checkbox">Blue eyes</label>
        </div>
        <div class="col-4 form-check">
          <input type="checkbox" class="form-check-input" id="brown_eye_checkbox" name="brown_eye_checkbox">
          <label class="form-check-label" for="brown_eye_checkbox">Brown eyes</label>
        </div>
        <div class="col-4 form-check">
          <input type="checkbox" class="form-check-input" id="green_eye_checkbox" name="green_eye_checkbox">
          <label class="form-check-label" for="green_eye_checkbox">Green eyes</label>
        </div>
      </div>
      <hr>
      <div class="row mb-3">
        <div class="col-4 form-check">
          <input type="checkbox" class="form-check-input" id="dark_hair_checkbox" name="dark_hair_checkbox">
          <label class="form-check-label" for="dark_hair_checkbox">Dark hair</label>
        </div>
        <div class="col-4 form-check">
          <input type="checkbox" class="form-check-input" id="blonde_hair_checkbox" name="blonde_hair_checkbox">
          <label class="form-check-label" for="blonde_hair_checkbox">Blonde hair</label>
        </div>
        <div class="col-4 form-check">
          <input type="checkbox" class="form-check-input" id="ginger_hair_checkbox" name="ginger_hair_checkbox">
          <label class="form-check-label" for="ginger_hair_checkbox">Ginger hair</label>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Submit preferences</button>
    </form>

    <h1>Recommended Matches</h1>
    <hr>
    <br><br>
    <alert :message="message" v-if="showMessage"/>

    <div class="container">
      <div class="row row-cols-3">
        <div class="col" v-for="(user, index) in users" :key="index">
          <user-details :user="user"/>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import Alert from './Alert.vue'
import UserDetails from "@/components/UserDetails";
import $ from 'jquery'

export default {
  name: "Index",

  beforeCreate() {
    if (!this.$session.exists())
      this.$router.push('/login')
  },

  data() {
    return {
      message: {},
      showMessage: false,
      users: [],
      path: 'http://localhost:5000/'
    }
  },

  components: {
    Alert,
    UserDetails,
  },

  methods: {
    getUsers() {
      axios.get(this.path).then((res) => {
            if (this.$session.get('user').type === 'free') {
              for (let i = 0; i < 3; i++) {
                this.users.push({
                  id: res.data.users[i]._id,
                  pfp: res.data.users[i].pfp,
                  username: res.data.users[i].username,
                  email: res.data.users[i].email,
                  name: res.data.users[i].name,
                  surname: res.data.users[i].surname,
                  birthday: res.data.users[i].birthday,
                  bio: res.data.users[i].bio,
                  gender: res.data.users[i].gender,
                  weight: res.data.users[i].weight,
                  height: res.data.users[i].height,
                  eye_colour: res.data.users[i].eye_colour,
                  hair_colour: res.data.users[i].hair_colour
                })
              }
            } else {
              res.data.users.forEach(user => {
                this.users.push({
                  id: user._id,
                  pfp: user.pfp,
                  username: user.username,
                  email: user.email,
                  name: user.name,
                  surname: user.surname,
                  birthday: user.birthday,
                  bio: user.bio,
                  gender: user.gender,
                  weight: user.weight,
                  height: user.height,
                  eye_colour: user.eye_colour,
                  hair_colour: user.hair_colour
                })
              })
            }
          }
      )
    },

    filterSearch(evt) {
      evt.preventDefault()
      let min_weight = $('#text_box_weight_minimum').val()
      let max_weight = $('#text_box_weight_maximum').val()
      let min_height = $('#text_box_height_minimum').val()
      let max_height = $('#text_box_height_maximum').val()
      let blue_eyes_option = $('#blue_eye_checkbox').is(':checked')
      let brown_eyes_option = $('#brown_eye_checkbox').is(':checked')
      let green_eyes_option = $('#green_eye_checkbox').is(':checked')
      let dark_hair_option = $('#dark_hair_checkbox').is(':checked')
      let blonde_hair_option = $('#blonde_hair_checkbox').is(':checked')
      let ginger_hair_option = $('#ginger_hair_checkbox').is(':checked')

      min_weight = (min_weight !== '') ? min_weight : null
      max_weight = (max_weight !== '') ? max_weight : null
      min_height = (min_height !== '') ? min_height : null
      max_height = (max_height !== '') ? max_height : null
      blue_eyes_option = blue_eyes_option ? "Blue" : null
      brown_eyes_option = brown_eyes_option ? "Brown" : null
      green_eyes_option = green_eyes_option ? "Green" : null
      dark_hair_option = dark_hair_option ? "Dark" : null
      blonde_hair_option = blonde_hair_option ? "Blonde" : null
      ginger_hair_option = ginger_hair_option ? "Ginger" : null

      let query = '{'
      let add_comma = false
      if (min_weight != null || max_weight != null) {
        query = query.concat('"weight": {')
        add_comma = true
        query = (min_weight != null) ? query.concat(`"$gte": ${min_weight}`) : query
        query = (max_weight != null) ? query.concat(`${(min_weight != null) ? ',' : ''}"$lte": ${max_weight}`) : query
        query = query.concat('}')
      }

      if (min_height != null || max_height != null) {
        if (add_comma)
          query = query.concat(',')
        else
          add_comma = true

        query = query.concat('"height": {')
        query = (min_height != null) ? query.concat(`"$gte": ${min_height}`) : query
        query = (max_height != null) ? query.concat(`${(min_height != null) ? ',' : ''}"$lte": ${max_height}`) : query
        query = query.concat('}')
      }

      if (blue_eyes_option != null || brown_eyes_option != null || green_eyes_option != null) {
        if (add_comma)
          query = query.concat(',')
        else
          add_comma = true

        query = query.concat('"eye_colour": {"$in": [')
        query = (blue_eyes_option != null) ? query.concat(`"${blue_eyes_option}"`) : query
        query = (brown_eyes_option != null) ? query.concat(`${(blue_eyes_option != null) ? ',' : ''}` +
            `"${brown_eyes_option}"`) : query
        query = (green_eyes_option != null) ? query.concat(
            `${(blue_eyes_option != null) ? ',' : (brown_eyes_option != null) ? ',' : ''}` +
            `"${green_eyes_option}"`) : query
        query = query.concat(']}')
      }

      if (dark_hair_option != null || blonde_hair_option != null || ginger_hair_option != null) {
        if (add_comma)
          query = query.concat(',')
        else
          add_comma = true

        query = query.concat('"hair_colour": {"$in": [')
        query = (dark_hair_option != null) ? query.concat(`"${dark_hair_option}"`) : query
        query = (blonde_hair_option != null) ? query.concat(`${(dark_hair_option != null) ? ',' : ''}` +
            `"${blonde_hair_option}"`) : query
        query = (ginger_hair_option != null) ? query.concat(
            `${(dark_hair_option != null) ? ',' : (blonde_hair_option != null) ? ',' : ''}` +
            `"${ginger_hair_option}"`) : query
        query = query.concat(']}')
      }
      query = query.concat('}')

      const payload = {
        filter: JSON.parse(query),
        prime: this.$session.get('user').type !== "free"
      }

      axios.post(this.path, payload).then((res) => {
        console.log(this.users)
        this.users = []
        res.data.users.forEach(user => {
          this.users.push({
            id: user._id,
            pfp: user.pfp,
            username: user.username,
            email: user.email,
            name: user.name,
            surname: user.surname,
            birthday: user.birthday,
            bio: user.bio,
            gender: user.gender,
            weight: user.weight,
            height: user.height,
            eye_colour: user.eye_colour,
            hair_colour: user.hair_colour
          })
        })
      })
    }
  },

  created() {
    this.getUsers()
  }
}
</script>

<style scoped>
</style>