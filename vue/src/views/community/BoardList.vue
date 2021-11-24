<template>
  <div>
    <header>
      <ul>
        <h1>익명 게시판</h1>
          <tr class="table-dark text-white">
          <th scope="col">영화 제목</th>
          <th scope="col">글 제목</th>
          <th scope="col">작성자</th>
          <th scope="col">작성 시간</th>
        </tr>
        <li v-for="board in boards" :key="`board_${board.id}`" @click="BoardListDetail(board.id)">
               {{ board.id }} 
               {{ board.title }} 
               {{ board.created_at }} 
        </li>
        <button @click="createBoard">게시글 작성</button>
      </ul>
    </header>
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

header{width:100%; text-align:center; position:relative; height:120px; border-bottom:1px solid #35495e}
header h1{position:absolute; top:0; left:100px;}
header ul.menu:after{display:block; clear:both; content:'';}
header ul.menu{position:absolute; top:20px; right:50px;}
header ul.menu li{float:left; padding:10px 20px; list-style:none;}
</style>