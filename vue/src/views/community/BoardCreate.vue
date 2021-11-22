<template>
  <div>
      <form action="">
        제목 : <input 
        type="text" 
        v-model.trim="board.title" 
        > <br>
        내용 : 
        
        <input 
        type="text" 
        v-model.trim="board.content" 
        > <br>
        <button @click="createBoard">작성하기</button>
        <button @click="backList">뒤로가기</button>
      </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'BoardCreate',
  data: function() {
    return {
      board:{
        title: '',
        content: '',
      }
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
    backList(){
      this.$router.push({ name:'BoardList' })
    },
    createBoard: function () {
      const config = this.getToken()
      axios.post(`http://127.0.0.1:8000/community/`, this.board, config)
        .then(() => {
          this.$router.push({ name:'BoardList' })
        })
        .catch((err) => {
          console.log(err)
        })
        }
    }
  }
</script>
  

