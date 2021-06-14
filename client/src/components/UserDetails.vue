<template>
  <div class="container shadow p-3 mb-4" style="color: white; background-color: #303030; border-radius: 20px;">
    <photo :user="user"/>

    <div class="mt-2 row">

      <button type="button" @click="goToProfile(user)"
              class="btn hide-text" style="width:100%; border: none !important; color: white;"
              role="button">
        <h4 class="hide-text">{{ user.name }} {{ user.surname }}</h4>
      </button>

    </div>
    <div class="mt-1 row">
      <h4 class="hide-text">{{ age }} years old</h4>
    </div>
    <div class="mt-1 row">
      <p class="hide-text" v-if="this.user.bio">{{ user.bio }}</p>
      <p v-else><br></p>
    </div>
    <div class="mt-1 row">
      <p class="hide-text">{{ user.gender }}</p>
    </div>
    <div class="mt-1 row">
      <p class="hide-text">{{ user.weight }}kg</p>
    </div>
    <div class="mt-1 row">
      <p class="hide-text">{{ user.height }}cm</p>
    </div>
    <div class="mt-1 row">
      <p class="hide-text">{{ user.eye_colour }} eyes</p>
    </div>
    <div class="mt-1 row">
      <p class="hide-text">{{ user.hair_colour }} hair</p>
    </div>
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

  methods: {
    goToProfile(user) {
      this.$router.push(`/profile/${user._id}`)
      // window.location.replace("/profile/" + user.id);
    }
  },

  created() {
    this.age = calculate_age(new Date(this.user.birthday))
  },
  updated() {
    this.age = calculate_age(new Date(this.user.birthday))
  },
  mounted() {
    this.age = calculate_age(new Date(this.user.birthday))
  }
}
</script>

