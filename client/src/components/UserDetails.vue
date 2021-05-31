<template>
  <div class="container">
    <h2>User Details</h2>
    <photo :user_photo="user.pfp" v-if="user.pfp"/>
    <p>Username: {{ user.username }}</p>
    <p>Name: {{ user.name }}</p>
    <p>Surname: {{ user.surname }}</p>
    <p>Age: {{ age }}</p>
    <p>Birthday: {{ user.birthday }}</p>
    <p v-if="user.bio">Bio: {{ user.bio }}</p>
    <p v-if="user.gender">Gender: {{ user.gender }}</p>
    <p v-if="user.weight">Weight: {{ user.weight }}kg</p>
    <p v-if="user.height">Height: {{ user.height }}m</p>
    <p v-if="user.eye_colour">Eye colour: {{ user.eye_colour }}</p>
    <p v-if="user.sexual_orientation">Sexual orientation: {{ user.sexual_orientation }}</p>
    <p v-if="user.education">Education: {{ user.education }}</p>
    <p v-if="user.smoker">Smokes</p>
    <p v-if="user.drinker">Drinks</p>
    <p v-if="user.children">Has children</p>
    <p v-if="user.status">Status: {{ user.status }}</p>
  </div>
</template>

<script>
import {calculate_age} from "@/ts/lib";
import Photo from "@/components/Photo";

export default {
  name: "UserDetails",

  data() {
    return {
      age: ''
    }
  },

  components: {
    Photo
  },

  props: ['user'],

  created() {
    this.age = calculate_age(new Date(this.user.birthday))
  }
}
</script>