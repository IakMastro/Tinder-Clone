<template>
  <div class="container">
    <h1>HELLO WORLD</h1>
    <table class="table forms-alt" style="vertical-align: middle;">
      <tr>
        <td>
          <div class="container">
            <div class="row justify-content-md-center">
              <div class="col-md-auto">
                <form action="" method="post">
                  <div class="d-flex justify-content-center">
                    <h1>Contact form</h1>
                  </div>
                  <div class="row">
                    <div class="mt-3 col-6">
                      <label class="form-label">Your email</label>
                      <p>{{ this.$session.get('user').email }}</p>
                    </div>
                    <div class="mt-3 col-6">
                      <label class="form-label">User's email</label>
                      <p>{{ this.user.email }}</p>
                    </div>
                  </div>
                  <div class="mt-3">
                    <label for="message" class="form-label">Your message</label>
                    <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
                  </div>
                  <div class="mt-3 d-flex align-items-center justify-content-between">
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <button type="button" @click="goToProfile(this.user)" class="btn btn-danger" role="button">
                      Cancel
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "Contact",

  data() {
    return {
      user: '',
      path: 'http://localhost:5000/user'
    }
  },

  props: ['user'],

  methods: {
    getUserInfo() {
      axios.get(this.path.concat(this.$route.params._id)).then((res) => {
        this.user = res.data.user
        console.log(this.user)
      })
    },

    goToProfile(user) {
      this.$router.push(`/profile/${user._id}`)
    }
  },

  created() {
    this.getUserInfo()
  }
}
</script>

<style scoped>

</style>