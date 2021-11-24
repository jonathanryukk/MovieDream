<template>
  <div class="wrapper fadeInDown">
    <div id="formContent">
      <!-- Tabs Titles -->

      <!-- Icon -->
      <br>
      <h2>Welcome To MovieDream</h2>
      <!-- Login Form -->
      <form>
        <input type="text" id="username" placeholder="username" v-model="credentials.username">
        <input type="text" id="password" placeholder="password" v-model="credentials.password">
        <input type="text" id="passwordConfirmation" placeholder="password confirmation" v-model="credentials.passwordConfirmation" @keypress.enter="login(credentials)">
      </form>

      <!-- Remind Passowrd -->
      <div id="formFooter">
        <a class="underlineHover" href="">
          <button @click="signup">회원가입</button>
        </a>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(() => {
          // console.log(res)
          this.$router.push({ name: 'Login'})
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
