<template>
  <div id="app">
    <div id="nav" class="card m-4" style="border: 1px solid rgb(78, 51, 62); background-color: white;">
      
      <div v-if="isLogin">
        <ul class="nav justify-content-start"> 
          <div class="items">
          <img src="@/moviedream.png" alt="moviedream" width="75px">
          <router-link :to="{ name: 'Home' }" class="fas fa-home font-weight-bolder " style="text-decoration:none"> Home</router-link> |
          <!-- <router-link :to="{ name: 'Recommend' }" class="fas fa-video font-weight-bolder " style="text-decoration:none"> Recommended Movie</router-link> | -->
          <!-- <router-link :to="{ name: 'Community' }" class="fas fa-comment font-weight-bolder " style="text-decoration:none"> Community</router-link> |  -->
          <router-link :to="{ name: 'BoardList' }"  class="fas fa-home font-weight-bolder">Board</router-link> |
           </div>
            <div class='column'>
              <div class='search'>
                <div class='search_bar'>
                  <input @keypress.enter="onInputSearch(keyword)" @input="submitAutoComplete" placeholder='영화제목 입력 후 enter!' type='text' v-model="keyword" autofocus >
                  <label for='searchOne' @click="cleanKeyword" style="margin:5px">
                    <i class="fas fa-search font-weight-bolder " ></i>
                  </label>
                </div>
                <div v-if="keyword" class="autocomplete disabled card m-1" style="width:300px; border: 2px solid rgb(76, 56, 192); background-color: black">
                  <div 
                    @click="searchSkillAdd(i)"
                      style="cursor: pointer"
                      v-for="(res,i) in result"
                      :key="i"
                      >{{ result[i] }}
                  </div>  
                </div>
              </div>
            </div>
          <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">
              내 정보 
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
              <li>
                <button class="dropdown-item" type="button" ></button>
                <router-link @click.native="logout" to="#">로그아웃</router-link> 
              </li>
              <li>
                <button class="dropdown-item" type="button"></button>
                <router-link :to="{ name: 'Profile' }">프로필</router-link> 
              </li>
            </ul>
          </div>
        </ul>

      </div>
      <span v-else>
        <router-link :to="{ name: 'Home' }">Home</router-link> |
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> |
      </span>

    </div>
    <router-view @login="isLogin=true"/>
  </div>
</template>

<script>

import skills from "@/skills.js";

export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      keyword : '',
      searchQuery: '',
      result: '',
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
        searchSkillAdd(i){
      this.keyword =this.result[i]

    },
    cleanKeyword(){
      this.keyword = ''

    },
    submitAutoComplete() {
      if (this.keyword) {
        this.result = skills.filter((skill) => {
          return skill.match(new RegExp("^" + this.keyword, "i"))         
        })
      } 
    },

    onInputSearch: function (keyword) {
     this.$router.push({name: 'SearchBar', query: {keyword: keyword}})
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

.search_bar {
  width: 580px;
  position: relative;
  margin: 0 auto;
}



</style>
