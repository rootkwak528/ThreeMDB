<template>
  <div id="tmdb-outer-window">
    <div id="tmdb-inner-window">

      <div>
        <TmdbLikedList 
          :likedMovies="likedMovies"
          @clickLikedCard="clickLikedCard"
        />
      </div>

      <div v-if="likedMovies[2] === ''">
        <!-- <TmdbLikedMovies/> -->
        <TmdbSearchBox
          :searchInit="searchInit"
          @onTmdbTextInput="onTmdbTextInput"
          @textResetComplete="onTextResetComplete"
        />
        <TmdbSearchList
          :movieList="movieList"
          @clickCard="initSearchBoxAndList"
        />
      </div>

      <div v-else>
        <TmdbSubmitButton
          @clickSubmit="clickSubmit"
        />
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

import TmdbLikedList from '@/components/TmdbSearch/TmdbLikedList'
import TmdbSearchBox from '@/components/TmdbSearch/TmdbSearchBox'
import TmdbSearchList from '@/components/TmdbSearch/TmdbSearchList'
import TmdbSubmitButton from '@/components/TmdbSearch/TmdbSubmitButton'

import { mapActions } from 'vuex'

const API_URL = 'https://api.themoviedb.org/3'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY

export default {
  name: 'TmdbSearch',
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

  created () {
    const token = localStorage.getItem('jwt')
    
    if ( !token ) {

      this.set_errors( '먼저 로그인을 해야 합니다.' )
      this.$router.push({ name: 'Login' })

    }
  },

  methods: {
    ...mapActions([
      'set_errors',
    ]),

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
      this.$router.push({ name: 'MovieRecommend' })
    },

    onTextResetComplete () {
      this.searchInit = false
    },
    
    onTmdbTextInput (textInput) {
      if (textInput) {

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

      } else {
        this.movieList = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
      }
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
#tmdb-outer-window {
  padding-top: 100px;
  background-color: white;
  height: 100vh;
}

#tmdb-inner-window {
  background-color: white;
}
</style>