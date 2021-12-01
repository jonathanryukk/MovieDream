<template>
  <div>
    <h1>Detail</h1>
      <div class="card text-black bg-white mb-3" style="max-width: 150rem; margin-left:300px; margin-right:300px; margin-top:20px;">
        <h3 class="card-header">제목 :  {{ boardDetail.title }}</h3>
        <div class="card-body">
          <p class="card-title"> {{ boardDetail.created_at }}</p>
          <p class="card-text"> 내용 : {{ boardDetail.content }} </p>
          <h4>Comment</h4>
          <div v-for="(comment, idx) in comments" :key="idx">
            {{comment.content}} 
          </div>
        </div>
      </div>
  </div>
  
</template>
<script>
import axios from 'axios'


export default {
  name: 'BoardListDetail',
  data() {
    return {
      boardDetail: [],
      boardId: this.$route.params.boardId,
      comment_content: '',
      comments: [Array, Object],
      user: [],
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
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
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

    getComments: function () { //댓글 가져오기
      const config = this.getToken()
      axios.get(`http://127.0.0.1:8000/community/${this.boardId}/board_comment_list_or_create/`, config)
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    createComment: function () { //댓글생성
      const config = this.getToken()
      const commentItem = {
        content: this.comment_content,
      }
      if (commentItem.content) {
          axios.post(`http://127.0.0.1:8000/community/${this.boardId}/comments/`, commentItem, config)
          .then( () => {
            this.getComments()
            this.comment_content = ''
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  },
  computed: {
    commentsList: function () {
      // console.log('댓글입니다')
      // console.log(this.comments)
      return this.comments
    }
  },
  created: function () {
    this.getBoardDetail()
    this.getComments()
  }
}


</script>

<style>

</style>