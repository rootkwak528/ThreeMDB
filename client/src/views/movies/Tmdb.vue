<template>
  <div id="tmdb-window">

    <div>
      <LikedThreeMovieCards 
        :likedMovies="likedMovies"
      />
    </div>

    <div>
      <!-- <TmdbLikedMovies/> -->
      <TmdbSearchBox
        @tmdb-text-input="onTmdbTextInput"
        :searchInit="searchInit"
        @textResetComplete="onTextResetComplete"
      />
      <TmdbDetail
        :selectedMovie="selectedMovie"
        @initialize="initSearchBoxAndList"
      />
      <TmdbSearchList
        :movieList="movieList"
        @on-click-item="onClickItem"
        @clickCard="initSearchBoxAndList"
      />
    </div>

  </div>
</template>

<script>
import axios from 'axios'

import TmdbDetail from '@/components/TmdbDetail'
import TmdbSearchBox from '@/components/TmdbSearchBox'
import TmdbSearchList from '@/components/TmdbSearchList'
import LikedThreeMovieCards from '@/components/LikedThreeMovieCards'

const API_URL = 'https://api.themoviedb.org/3'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name: 'Tmdb',
  data () {
    return {
      selectedMovie: '',
      movieList: ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
      searchInit: false,
      likedMovies: [],
    }
  },
  components: {
    TmdbDetail,
    TmdbSearchBox,
    TmdbSearchList,
    LikedThreeMovieCards,
  },
  methods: {
    initSearchBoxAndList (likedMovie) {
      this.likedMovies.push(likedMovie)
      console.log('receive', this.likedMovies)
      this.movieList = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
      this.selectedMovie = ''
      this.searchInit = true
    },
    onTextResetComplete () {
      this.searchInit = false
    },
    onTmdbTextInput (textInput) {
      const params = {
        region: 'KR',
        language: 'ko',
        query: textInput
      }
      
      // TMDB 검색
      this.searchTMDB('search', 'movie', params)
        .then( res => {
          // console.log(res)
          const results = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
          let idx = 0
          res.data.results.forEach(movie => {
            if (movie.poster_path) {
              results[idx] = movie
              idx += 1
            }
          })
          this.movieList = results
        })
        .catch( err => {
          console.log(err)
        })
    },
    onClickItem (movie) {
      // TMDB 예고편 정보 확인
      this.searchTMDB('movie', `${movie.id}/videos`)
        .then( () => {
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
#tmdb-window {
  padding-top: 100px;
}
</style>