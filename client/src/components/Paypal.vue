<template>
  <div class="container">
    <hr>
    <div class="row">
      <div class="col d-flex flex-column justify-content-center align-items-center" style="text-align:center;">
        <div id="paypal-button-container" style="width: 35%"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: "Paypal",

  methods: {
    logout() {
      this.$session.destroy()
      this.$router.push('/login')
    }
  },

  created() {
    axios.put("http://localhost:5000/prime/".concat(this.$session.get('user')._id)).then(() => console.log('done'))
    this.$session.get('user').type = 'premium'
    setTimeout(function () {
      window.location.replace("/settings?primePaid=1");
    }, 1000);
  }
}
</script>
<style scoped>

</style>