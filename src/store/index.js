import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

import router from '@/router/index.js'
import SERVER from '@/api/drf.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieDetail: null,
    errors: null,
  },

  getters: {

  },

  mutations: {

    SET_TOKEN (state, token) {
      localStorage.setItem('jwt', token)
      state.authToken = token
    },

    REMOVE_TOKEN (state) {
      localStorage.removeItem('jwt')
      state.authToken = localStorage.getItem('jwt')
    },

    SET_ERRORS (state, errors) {
      state.errors = errors
      console.log('err:', state.errors)
    },

  },

  actions: {

    signup ({ commit, dispatch }, credentials) {
      dispatch('set_errors', null)
    
      axios({
        url: SERVER.URL + SERVER.ROUTES.signup,
        method: 'post',
        data: credentials,
      })
        .then(res => {
          commit('SET_TOKEN', res.data.token)
          router.push({ name: 'TmdbSearch' })
        })
        .catch(err => {
          console.log(err)
          if (err.response.data.error) {
            dispatch('set_errors', err.response.data.error)
          } else if (err.response.data.username) {
            dispatch('set_errors', err.response.data.username[0])
          }
        })
    },

    login ({ commit, dispatch }, credentials) {
      dispatch('set_errors', null)
      
      axios({
        url: SERVER.URL + SERVER.ROUTES.login,
        method: 'post',
        data: credentials,
      })
        .then(res => {
          commit('SET_TOKEN', res.data.token)
          router.push({ name: 'TmdbSearch' })
        })
        .catch(err => {
          console.log(err)
          dispatch('set_errors', 'ID와 비밀번호를 확인해주세요.')
        })
    },

    logout ({ commit }) {
      commit('REMOVE_TOKEN')
    },

    set_errors ({ commit }, errors ) {
      commit('SET_ERRORS', errors)
    },

  },

  plugins: [createPersistedState()],
})