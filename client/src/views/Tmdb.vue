<template>
  <div>
    <!-- <TmdbLikedMovies/> -->
    <TmdbSearchBox
      @tmdb-text-input="onTmdbTextInput"
    />
    <TmdbDetail
      :selectedMovie="selectedMovie"
    />
    <TmdbSearchList
      :movieList="movieList"
      @on-click-item="onClickItem"
    />
  </div>
</template>

<script>
import axios from 'axios'

import TmdbDetail from '@/components/TmdbDetail'
import TmdbSearchBox from '@/components/TmdbSearchBox'
import TmdbSearchList from '@/components/TmdbSearchList'

const API_URL = 'https://api.themoviedb.org/3'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name: 'Tmdb',
  data () {
    return {
      selectedMovie: '',
      movieList: ''
    }
  },
  components: {
    TmdbDetail,
    TmdbSearchBox,
    TmdbSearchList
  },
  methods: {
    onTmdbTextInput (textInput) {
      const params = {
        region: 'KR',
        language: 'ko',
        query: textInput
      }
      
      // TMDB 검색
      this.searchTMDB('search', 'movie', params)
        .then( res => {
          this.movieList = res.data.results
        })
        .catch( err => {
          console.log(err)
        })
    },
    onClickItem (movie) {
      // TMDB 예고편 정보 확인
      this.searchTMDB('movie', `${movie.id}/videos`)
        .then( () => {
          // let trailerUrl = ''
          // try {
          //   trailerUrl = `https://www.youtube.com/embed/${res.data.results[0].key}`
          // }
          // catch (err) {
          //   console.log(err)
          // }
          // this.selectedMovie = {
          //   ...movie,
          //   trailerUrl
          // }
          this.selectedMovie = movie
        })
        .catch( err => {
          console.log(err)
        })
    },
    async searchTMDB (category, feature, params) {
      // url 확인
      let url = `${API_URL}/${category}/${feature}?api_key=${API_KEY}`
      for (const key in params) {
        url += `&${key}=${params[key]}`
      }

      // TMDB API request
      return await axios({
        method: 'get',
        url
      })
    }
  }
}
</script>

<style>

</style>