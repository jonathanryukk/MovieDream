import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import BoardList from '@/views/community/BoardList'
import BoardListDetail from '@/views/community/BoardListDetail'
import BoardCreate from '@/views/community/BoardCreate'


Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/community/boardlist',
    name: 'BoardList',
    component: BoardList
  },
  {
    path: '/community/boardlistDetail/:boardId',
    name: 'BoardListDetail',
    component: BoardListDetail
  },
  {
    path: '/community/boardcreate',
    name: 'BoardCreate',
    component: BoardCreate
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
