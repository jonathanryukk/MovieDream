<template>
  <div>
    <h1>자유 게시판</h1>
    <div align="right" style="margin-right:50px">
      <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">게시글 작성</button>
    </div>
    <header>
      <div>
        <table class="table table-hover tablesetting">
          <thead>
            <tr>
              <th scope="col">게시글 번호</th>
              <th scope="col">제목</th>
              <th scope="col">자세히</th>
            </tr>
          </thead>
          <tbody v-for="board in boards" :key="`board_${board.id}`">
            <tr class="table-light">
                <td> {{ board.id}} </td>
                <td> {{ board.title}} </td>
                <td> {{ board.created_at}} </td>
                <td @click="BoardListDetail(board.id)"> Detail </td>
            </tr>
          </tbody>
        </table>
        <div>
        <ul class="pagination">
          <li class="page-item disabled">
            <a class="page-link" href="#">&laquo;</a>
          </li>
          <li class="page-item active">
            <a class="page-link" href="#">1</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">2</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">3</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">4</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">5</a>
          </li>
          <li class="page-item">
            <a class="page-link" href="#">&raquo;</a>
          </li>
        </ul>
      </div>
      </div>
    </header>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">게시글 작성</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">제목:</label>
            <input type="text" v-model.trim="board1.title" placeholder="제목을 입력해주세요">
          </div>
          <div class="mb-3">
            <label for="message-text" class="col-form-label">내용:</label>
            <textarea type="text" class="form-control" v-model.trim="board1.content" id="message-text"></textarea>
          </div>
        </form>
      </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="createBoard" data-bs-dismiss="modal">Post</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'BoardList',
  data: function () {
    return {
      boards: [],
      board1:{
        title: '',
      content: '',
      }
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
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers:{
          Authorization: `JWT ${token}`
        }
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
        headers: this.getToken() // Authorization: JWT tokensdjiadnoiqwnd
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
      const config = this.setToken()
      axios.post(`http://127.0.0.1:8000/community/`, this.board1, config)
        .then(() => {
          this.BoardListDetail(this.boards[this.boards.length -1].id)
        })
        .catch((err) => {
          console.log('게시글 작성에 실패하였습니다.')
          console.log(err)
          
        })
      }  
  },
  created: function () {
  this.getBoardDetail()
  this.getComments()
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

.pagination{
  justify-content: center;
  justify-items: center;
}


.table-hovor{
  display: block;
  margin: 10%;
  padding: 5%;
  width: 400px;
  max-width: 100%;
  height: auto !important;
  border: 2px solid black;

}

</style>