<template>
  <div id="app">
    <h1>Tinder Clone mark 1</h1>

    <div class="header" v-if="this.$session.exists()">
      <div id="nav">
        <router-link to="/">Home</router-link>
        |
        <router-link to="/prime">Get Prime</router-link>
      </div>

      <h1>Hello {{ this.$session.get('user')['username'] }}</h1>
      <button class="btn btn-primary" @click="logout">Log out</button>
    </div>

    <div class="content">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$session.destroy()
      this.$router.push('/login')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
