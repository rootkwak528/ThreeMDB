<template>
  <div id="tmdb-window">

    <div>
      <TmdbLikedList 
        :likedMovies="likedMovies"
        @clickLikedCard="clickLikedCard"
      />
    </div>

    <div v-if="likedMovies[2] === ''">
      <!-- <TmdbLikedMovies/> -->
      <TmdbSearchBox
        @tmdb-text-input="onTmdbTextInput"
        :searchInit="searchInit"
        @textResetComplete="onTextResetComplete"
      />
      <TmdbSearchList
        :movieList="movieList"
        @on-click-item="onClickItem"
        @clickCard="initSearchBoxAndList"
      />
    </div>

    <div v-else>
      <TmdbSubmitButton
        @clickSubmit="clickSubmit"
      />
    </div>

  </div>
</template>

<script>
import axios from 'axios'

import TmdbLikedList from '@/components/Tmdb/TmdbLikedList'
import TmdbSearchBox from '@/components/Tmdb/TmdbSearchBox'
import TmdbSearchList from '@/components/Tmdb/TmdbSearchList'
import TmdbSubmitButton from '@/components/Tmdb/TmdbSubmitButton'

const API_URL = 'https://api.themoviedb.org/3'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name: 'Tmdb',
  data () {
    return {
      selectedMovie: '',
      movieList: ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
      searchInit: false,
      likedMovies: ['', '', '',],
    }
  },
  components: {
    TmdbSearchBox,
    TmdbSearchList,
    TmdbLikedList,
    TmdbSubmitButton,
  },
  methods: {
    initSearchBoxAndList (likedMovie) {
      let newLikedMovies = ['', '', '',]
      for (let i=0; i<3; i++) {
        if (!this.likedMovies[i]) {
          newLikedMovies[i] = likedMovie
          break
        } else if (this.likedMovies[i].title === likedMovie.title) {
          newLikedMovies = this.likedMovies
          break
        } else {
          newLikedMovies[i] = this.likedMovies[i]
        }
      }
      this.likedMovies = newLikedMovies

      this.movieList = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ],
      this.selectedMovie = ''
      this.searchInit = true
    },

    clickLikedCard ( likedMovie ) {
      const newLikedMovies = ['', '', '',]
      let i = 0, j = 0
      while (i < 3) {
        if (this.likedMovies[i] && this.likedMovies[i] !== likedMovie) {
          newLikedMovies[j] = this.likedMovies[i]
          i++
          j++
        } else {
          i++
        }
      }
      this.likedMovies = newLikedMovies
    },

    clickSubmit () {
      const likedMoviesJson = JSON.stringify(this.likedMovies)
      localStorage.setItem('likedMovies', likedMoviesJson)
      this.$router.push('movies/recommend')
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