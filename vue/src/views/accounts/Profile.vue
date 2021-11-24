<template>
  <div>
    <h1>profile</h1>
    <h5>이름: {{ user.username }}</h5>
    <h5>좋아요한 영화: {{ like }}</h5>
    <h5>팔로우중인사람: {{ followers }}</h5>
    <h5>팔로잉한사람: {{ follwings }}</h5>
  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from 'vue-jwt-decode'

export default {
  name: "Profile",
  data: function () {
    return {
      user: '',
      like: [],
      userrank: [],
      followers: [],
      follwings: [],   
    }
  },
  methods:{
    getTokeon: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization:`JWT ${token}`
        }
      }
      return config
    },

    getUser: function () {
      const config = this.getTokeon()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post('http://127.0.0.1:8000/accounts/profile/', info, config)
      .then( (res) => {
        console.log(res)

        this.user = res.data
        this.like = res.data.like_movies
        this.userrank = res.data.user_rank
        this.follwings = res.data.followings[0].username
        this.followers = res.data.followers[0].username
      })
    }
  },
  created() {
    this.getUser()
  }
}
</script>

<style>

</style>