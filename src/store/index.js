import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

import router from '@/router/index.js'
import SERVER from '@/api/drf.js'

const API_URL = 'https://api.themoviedb.org/3'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY
const SERVER_URL = process.env.VUE_APP_SERVER_URL

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    // accounts
    errors: null,
    
    // tmdb search
    likedMovies: ['', '', '', ],
    searchInput: '',
    searchResults: ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],

    // recommend - three.js
    movieRecommends: null,
    movieDetail: null,
  },

  getters: {

  },

  mutations: {

    // accounts
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
    },

    // tmdb search
    SET_SEARCH_INPUT (state, searchInput) {
      state.searchInput = searchInput
    },

    SET_SEARCH_RESULTS (state, searchResults) {
      state.searchResults = searchResults
    },

    SET_LIKED_MOVIES (state, likedMovies) {
      state.likedMovies = likedMovies
    },

    ADD_CARD (state, movie) {
      let newLikedMovies = ['', '', '',]

      for (let i=0; i<3; i++) {
        if (!state.likedMovies[i]) {
          newLikedMovies[i] = movie
          state.searchInput = ''
          state.searchResults = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
          break

        } else if (state.likedMovies[i].id == movie.id) {
          newLikedMovies = state.likedMovies
          break

        } else {
          newLikedMovies[i] = state.likedMovies[i]

        }
      }
      state.likedMovies = newLikedMovies
    },

    REMOVE_CARD (state, movie) {
      const newLikedMovies = ['', '', '',]

      let j = 0
      for (let i=0; i<3; i++) {
        const ithLikedMovie = state.likedMovies[i]
        if (ithLikedMovie && ithLikedMovie !== movie) {
          newLikedMovies[j] = ithLikedMovie
          j++
        }
      }
      state.likedMovies = newLikedMovies
    },

    RESET_SEARCH (state) {
      state.searchInput = ''
      state.searchResults = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
      state.likedMovies = ['', '', '', ]
    },

    // recommend - three.js
    SET_MOVIE_RECOMMENDS (state, movieRecommends) {
      state.movieRecommends = movieRecommends
    },

    SET_MOVIE_DETAIL (state, movieDetail) {
      state.movieDetail = movieDetail
    },
  },

  actions: {

    // accounts
    signup ({ commit, dispatch }, credentials) {
      dispatch('setErrors', null)
    
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
            dispatch('setErrors', err.response.data.error)
          } else if (err.response.data.username) {
            dispatch('setErrors', err.response.data.username[0])
          }
        })
    },

    login ({ commit, dispatch }, credentials) {
      dispatch('setErrors', null)
      
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
          dispatch('setErrors', 'ID와 비밀번호를 확인해주세요.')
        })
    },

    logout ({ commit }) {
      commit('REMOVE_TOKEN')
    },

    setErrors ({ commit }, errors ) {
      commit('SET_ERRORS', errors)
    },

    // tmdb search
    setSearchInput ({ commit }, searchInput ) {
      const trimmedSearchInput = searchInput.trim()
      commit( 'SET_SEARCH_INPUT', trimmedSearchInput )
      
      if ( trimmedSearchInput ) {
        let url = `${API_URL}/search/movie?api_key=${API_KEY}`

        const params = {
          region: 'KR',
          language: 'ko',
          query: trimmedSearchInput,
        }

        for (const key in params) {
          url += `&${key}=${params[key]}`
        }

        axios({
          url: url,
          method: 'get',
        })
          .then( res => {
            const results = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
            let idx = 0
            res.data.results.forEach(movie => {
              if (movie.poster_path) {
                results[idx] = movie
                idx += 1
              }
            })
            commit( 'SET_SEARCH_RESULTS', results )
          })
          .catch( err => {
            console.log(err)
          })

      } else {
        const results = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
        commit( 'SET_SEARCH_RESULTS', results )
      }
    },

    setLikedMovies ({ commit }, likedMovies ) {
      commit('SET_LIKED_MOVIES', likedMovies)
    },

    addCard ({ commit }, movie ) {
      commit('ADD_CARD', movie )
    },

    removeCard ({ commit }, movie ) {
      commit('REMOVE_CARD', movie )
    },

    resetSearch ({ commit }) {
      commit('RESET_SEARCH')
    },

    // recommend - three.js
    async getRecommends ({ commit }, movieId) {
      const url = `https://api.themoviedb.org/3/movie/${movieId}/recommendations?api_key=${API_KEY}&language=ko-KR&page=1`

      await axios({
        url: url,
        method: 'get',
      })
        .then( res => {
          if (res.data.results) {
            commit('SET_MOVIE_RECOMMENDS', res.data.results)
          } else {
            commit('SET_MOVIE_RECOMMENDS', null)
          }
        })
        .catch( err => {
          console.log(err)
          commit('SET_MOVIE_RECOMMENDS', null)
        })
    },

    async getDetail ({ commit }, movie ){
      const url = `${SERVER_URL}/movies/`

      await axios({
        url: url,
        method: 'post',
        data: movie,
      })
        .then( res => {
          commit('SET_MOVIE_DETAIL', res.data)
        })
        .catch( err => {
          console.log( err )
          commit('SET_MOVIE_DETAIL', null)
        })
    },
  },

  plugins: [createPersistedState()],
})