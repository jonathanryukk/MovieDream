<template>
  <div id="app">
    <div id="nav">
      <b-navbar toggleable="lg" type="dark" variant="dark" class="ml-5 mr-5">
        <span v-if="isLogin">
          <router-link @click.native="logout" to="#">로그아웃</router-link>|
          <router-link :to="{ name: 'BoardList' }">Board</router-link> 
          <form action="">
            검색 : <input @keypress.enter="search(keyword)" 
            type="text" 
            placeholder="키워드를 입력하세요."
            v-model="keyword" 
            autofocus>
          </form>
        </span>
        <span v-else>
          <router-link :to="{ name: 'Signup' }">Signup</router-link> |
          <router-link :to="{ name: 'Login' }">Login</router-link> |
          <router-link :to="{ name: 'BoardList' }">Board</router-link> 
        </span>
      </b-navbar>
      <router-view @login="isLogin=true"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
    search: function (keyword) {
    this.$router.push({name: 'SearchMovieList', query: {keyword: keyword}})
    this.keyword = ''
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')

    if (token) {
      this.isLogin = true
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