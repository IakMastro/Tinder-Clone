<template>
  <div class="container">
    <h1>Recommended Matches</h1>
    <hr>
    <br><br>
    <alert :message="message" v-if="showMessage"/>

    <ul>
      <li v-for="(user, index) in users" :key="index">
        {{ user.name }} {{ user.surname }} <b>{{ user.age }}</b>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from './Alert.vue'
import {calculate_age} from '@/ts/lib'

export default {
  name: "Index",

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
  },

  methods: {
    getUsers() {
      axios.get(this.path).then((res) => {
        res.data.users.forEach(user => {
          this.users.push({
            email: user.email,
            name: user.name,
            surname: user.surname,
            age: calculate_age(new Date(user.birthday))
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