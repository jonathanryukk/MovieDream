<template>
  <div>
    <ul>
      <h1>익명 게시판</h1>
      <li v-for="board in boards" :key="`board_${board.id}`" @click="BoardListDetail(board.id)">
            게시글 번호 : {{ board.id }} |
            제목 : {{ board.title }} |
            생성 날짜 : {{ board.created_at }} |
      </li>
      <button @click="createBoard">게시글 작성</button>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'BoardList',
  data: function () {
    return {
      boards: [],
    }
  },
  mounted() {
    if (localStorage.getItem('jwt')) {
      this.getBoards()
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
    BoardListDetail(board_id){
      this.$router.push({ name: 'BoardListDetail', params: {boardId:board_id}})
    },
    getBoards: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/',
        headers: this.setToken() // Authorization: JWT tokensdjiadnoiqwnd
      })
        .then(res => {
          console.log(res)
          this.boards = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    createBoard: function () {
      this.$router.push({ name: 'BoardCreate' })
    },    
  }
}
</script>

<style scoped>
  .board-btn {
    margin-left: 10px;
  }

  .is-completed {
    text-decoration: line-through;
    color: rgb(112, 112, 112);
  }
</style>