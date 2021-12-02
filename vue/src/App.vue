<template>
  <div id="app">
    <div id="nav" class="card m-4" style="border: 2px solid rgb(78, 51, 62); background-color: white;">
      
      <div v-if="isLogin">
        <ul class="nav" style="padding: 10px;"> 
          <div class="items">
            <img class="moviedream" src="@/moviedream.png" alt="moviedream" width="50px">
            <router-link :to="{ name: 'Home' }" class="fas fa-home font-weight-bolder effect-underline" style="text-decoration:none; margin:10px; font-xize: medium" > Home</router-link> 
            <router-link :to="{ name: 'Recommend' }" class="fas fa-video font-weight-bolder effect-underline" style="text-decoration:none; margin:10px"> Recommended Movie</router-link> 
            <router-link :to="{ name: 'BoardList' }" class="fas fa-comment font-weight-boldereffect-underline " style="text-decoration:none; margin:10px"> Community</router-link> 
          </div>
          <div class="items2">
            <div class='search' >
              <div class='search_bar'>
                <input @keypress.enter="onInputSearch(keyword)" @input="submitAutoComplete" placeholder='영화제목 입력 후 enter!' type='text' v-model="keyword" autofocus >
                <label for='searchOne' @click="cleanKeyword" style="margin:8px">
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
<li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <i class="fas fa-user"></i>
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li>
              <a class="dropdown-item" href="#"><i class="fas fa-sliders-h fa-fw"></i>
            <router-link @click.native="profile" to="#" style="text-decoration:none;" >Profile</router-link>
              </a>
            </li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#"><i class="fas fa-sign-out-alt fa-fw"></i> 
            <router-link @click.native="logout" to="#" style="text-decoration:none;" >Log out</router-link></a></li>
          </ul>
        </li>
            <!-- <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">
                내 정보 
              </button>
              <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
                <li class="dropdown-menu2">
                  <button class="dropdown-item" type="button" ></button>
                  <router-link @click.native="logout" to="#" style="text-decoration:none;" ></router-link> 
                </li>
                <li class="dropdown-menu2">
                  <button class="dropdown-item" type="button" ></button>
                  <router-link :to="{ name: 'Profile' }" style="text-decoration:none;" >프로필</router-link> 
                </li>
              </ul>
            </div> -->
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
    <footer>
      <p>copyright: Hyun-Jin Ryu<br>
      <a href="mailto:h14cdp@naver.com">h14cdp@naver.com</a></p>  
      <div class="social-icons">
            <div class="d-flex flex-row flex-lg-column justify-content-center align-items-center h-100 mt-3 mt-lg-0">
                <a class="btn btn-dark m-3" href="https://github.com/jonathanryukk"><i class="fab fa-github"></i></a>
            </div>
      </div>
    </footer>
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
  padding: 0px;
  
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.items a {
  font-size: 20px;
  transition: .3s all ease-in;
}

footer {
  margin-top: 70px;
  text-align: center;
  padding: 3px;
  background-color: white;
  color: black;
}

.items a:hover {
  transform: translateY(-5px);
}

.nav {
  display: flex;
  justify-content: space-between;
}

.items2 {
  display: flex;
}
.search_bar {
  /* position: relative; */
  margin: 20px 0;
  margin-left: 250px;
  display: flex;
  align-items: center;
}

.column {
  justify-items: center;
  justify-content: center;
  margin: 40px;
}

.dropdown {
  justify-items: center;
  justify-content: flex-end;
  margin-top: 40px;
  padding: 30;
  margin-left: 30px;
  margin-right: 20px;
}

.dropdown-menu2 {
  justify-content: center;
  margin-left: 40px;
  text-decoration:none;
}

.moviedream{
  padding: 5px;
  margin: 5px;
  justify-content: space-between;
  width: 100px;
  height: auto;
}


.profile-menu.dropdown-menu{
    right: 0;
    left: unset;
  }
  .fa-fw{
    margin-right: 10px;
  }  

.toggle-change{
&::after {
    border-top: 0;
    border-bottom: .3em solid;
    }
} 

</style>
