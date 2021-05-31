<template>
  <div class="container">
    <h1>Recommended Matches</h1>
    <hr>
    <br><br>
    <alert :message="message" v-if="showMessage"/>

    <ul>
      <li v-for="(user, index) in users" :key="index">
        <user-details :user="user"></user-details>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from './Alert.vue'
import UserDetails from "@/components/UserDetails";
import {calculate_age} from '@/ts/lib'

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
    UserDetails
  },

  methods: {
    getUsers() {
      axios.get(this.path).then((res) => {
        res.data.users.forEach(user => {
          this.users.push({
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
            sexual_orientation: user.sexual_orientation,
            education: user.education,
            smoker: user.smoker,
            drinker: user.drinker,
            children: user.children,
            status: user.status,
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