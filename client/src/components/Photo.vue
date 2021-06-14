<template>
  <div class="d-flex justify-content-center">
    <button type="button" @click="goToProfile(user)" class="btn shadow-none"
            style="border: none; overflow:hidden; border-radius: 20px; padding: 0px;" role="button">
      <img :src="this.photo.source" v-if="this.photo.source"
           style="position: relative; left:50%; transform: translateX(-50%);" height="400">
      <img src="@/assets/default.jpg" v-else alt="">
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Photo",

  data() {
    return {
      photo: ''
    }
  },

  props: ['user'],

  methods: {
    goToProfile(user) {
      // this.$router.push(`/profile/${user.id}`)
      window.location.replace("/profile/" + user.id);
    },
  },

  created() {
    axios.get(`http://localhost:5000/img/${this.user.pfp}`, {responseType: 'arraybuffer'})
        .then((res) => {
          const base64 = btoa(new Uint8Array(res.data)
              .reduce((data, byte) => data + String.fromCharCode(byte), ''))
          this.photo = ({source: "data:;base64," + base64})
        })
  },

  updated() {
    axios.get(`http://localhost:5000/img/${this.user.pfp}`, {responseType: 'arraybuffer'})
        .then((res) => {
          const base64 = btoa(new Uint8Array(res.data)
              .reduce((data, byte) => data + String.fromCharCode(byte), ''))
          this.photo = ({source: "data:;base64," + base64})
        })
  },

  mounted() {
    axios.get(`http://localhost:5000/img/${this.user.pfp}`, {responseType: 'arraybuffer'})
        .then((res) => {
          const base64 = btoa(new Uint8Array(res.data)
              .reduce((data, byte) => data + String.fromCharCode(byte), ''))
          this.photo = ({source: "data:;base64," + base64})
        })
  }
}
</script>

<style scoped>

</style>