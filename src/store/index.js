import Vue from 'Vue'
import Vuex from 'Vuex'
import createPersistedState from 'veux-persistedstate'

Vue.use(Vuex)

const store = new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {

  },
  mutations: {

  },
  actions: {

  },
  getters: {

  },
})