import Vue from 'vue'
import VueRouter from 'vue-router'

import Tmdb from '@/views/Tmdb'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieList from '@/views/movies/MovieList'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Tmdb',
    component: Tmdb
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
