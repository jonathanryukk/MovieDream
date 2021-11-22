<template>
  <div>
    <h1>Detail</h1>
      게시글 번호 : {{ boardDetail.id }} <br>
      제목 : {{ boardDetail.title }} <br>
      내용 : {{ boardDetail.content }} <br>
      작성 시간 : {{ boardDetail.created_at }}<br> 

  </div>
</template>
<script>
import axios from 'axios'


export default {
  name: 'BoardListDetail',
  data() {
    return {
      boardDetail: [],
      boardId: this.$route.params.boardId
    }
  },
  mounted() {
    if (localStorage.getItem('jwt')) {
        this.getBoardDetail()
    } else {
        this.$router.push({name: 'Login'})
        }
    },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getBoardDetail: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.boardId}/`,
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          this.boardDetail = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}


</script>

<style>

</style>