<template>
  <div id="app">
    <h1>MatchBox</h1>

    <div class="header" v-if="this.$session.exists()">
      <div id="nav">

        <router-link to="/">Home</router-link>
        |
        <router-link to="/settings">Account Settings</router-link>
        <div style="display: inline" v-if="this.$session.get('user').type!=='premium'"> |
          <router-link to="/prime">Get Prime</router-link>
        </div>
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
  /*font-family: Avenir, Helvetica, Arial, sans-serif;*/
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #757575;
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

.text-left {
  text-align: left !important;
}

.hide-text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.forms {
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
  overflow: hidden;
  border: hidden;
}

.forms-alt {
  height: 100%;
  width: 100%;
  padding: 0;
  margin: 0;
  overflow: visible;
  border: hidden;
}

.with_header {
  padding-top: 64px;
}
</style>
