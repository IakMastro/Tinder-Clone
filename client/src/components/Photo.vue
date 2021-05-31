<template>
  <div class="container">
    <img :src="this.photo.source" v-if="this.photo.source" alt="">
    <img src="@/assets/default.jpg" v-else alt="">
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

  props: ['user_photo'],

  created() {
    axios.get(`http://localhost:5000/img/${this.user_photo}`, {responseType: 'arraybuffer'})
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