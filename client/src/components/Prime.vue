<template>
  <div class="container">
    <hr>
    <div class="d-flex flex-column justify-content-center align-items-center container p-5 shadow"
         style="color: white; background-color: #303030; border-radius: 20px;">
      <div class="row">
        <h3>Plan</h3>
        <p>1 year plan: {{ price }}€</p>
      </div>
      <div class="row">
        <form @submit="checkReferral">
          <div class="mb-3 d-flex align-items-center justify-content-between">
            <div class="me-3 form-floating">
              <input type="text" class="form-control" id="referral" name="referral" placeholder="hi">
              <label for="referral" style="color: rgba(0, 0, 0, 0.5);">Referral code</label>
            </div>
            <button type="submit" class="btn btn-info">Check</button>
          </div>
        </form>
      </div>
      <div class="row d-flex flex-column align-items-center justify-content-between">
        <button class="btn btn-lg btn-success mb-1" @click="goToPaypal" style="width: auto;"><i
            class="bi bi-currency-exchange"></i> Buy
          Prime <i
              class="bi bi-currency-exchange"></i></button>
        <h4 class="mt-2">Your referral: {{ this.$session.get('user').username }}</h4>
        <p>Give your friends your referral code and they'll get 50% off their prime membership!</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import $ from 'jquery'

export default {
  name: "Prime",

  data() {
    return {
      price: 50,
      referral_code: ''
    }
  },

  methods: {
    checkReferral(evt) {
      evt.preventDefault()
      const referral_code = $('#referral').val()

      if (this.$session.get('user').username !== referral_code)
        axios.get('http://localhost:5000/referral/'.concat(referral_code)).then((res) => {
          if (res.data.message === 'OK') {
            if (this.price === 50)
              this.price /= 2;
            sessionStorage.setItem("prime_price", this.price);
          }
        })
    },
    goToPaypal() {
      window.location.replace("paypal");
      // this.$router.push(`/paypal`)
    },
  },

  created() {
    sessionStorage.setItem("prime_price", this.price);
  }
}
</script>

<style scoped>

</style>