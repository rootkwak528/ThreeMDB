<template>
  <div id="tmdb-outer-window">
    <div id="tmdb-inner-window">

      <div>
        <TmdbLikedList/>
      </div>

      <div v-if="likedMovies[2] === ''">
        <TmdbSearchBox/>
        <TmdbSearchList/>
      </div>

      <div v-else>
        <TmdbSubmitButton/>
      </div>

    </div>
  </div>
</template>

<script>
import TmdbLikedList from '@/components/TmdbSearch/TmdbLikedList'
import TmdbSearchBox from '@/components/TmdbSearch/TmdbSearchBox'
import TmdbSearchList from '@/components/TmdbSearch/TmdbSearchList'
import TmdbSubmitButton from '@/components/TmdbSearch/TmdbSubmitButton'

import { mapActions, mapState } from 'vuex'

export default {
  name: 'TmdbSearch',

  computed: {
    ...mapState([
      'likedMovies',
    ]),
  },

  methods: {
    ...mapActions([
      'setErrors',
      'resetSearch'
    ]),
  },

  components: {
    TmdbSearchBox,
    TmdbSearchList,
    TmdbLikedList,
    TmdbSubmitButton,
  },

  created () {
    const token = localStorage.getItem('jwt')
    if ( !token ) {

      this.setErrors( '먼저 로그인을 해야 합니다.' )
      this.$router.push({ name: 'Login' })

    } else {

      this.resetSearch()
    }
  },
}
</script>

<style>
#tmdb-outer-window {
  padding-top: 100px;
  background-color: white;
  height: 100vh;
}

#tmdb-inner-window {
  background-color: white;
}
</style>