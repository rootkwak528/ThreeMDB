<template>
  <div id="detail-window">
    
    <div class="col">
      <img  
        v-if="poster_path"
        :src="poster_path"
        alt="movie_poster"
      >
      <button class="position-absolute top-0 start-100" @click="close">x</button>
    </div>

    <ReviewForm 
      @reviewPost="reviewPost"
    />

    <ReviewList 
      :movie="movie"
      @reviewDelete="reviewDelete"
      @reviewPut="reviewPut"
    />

  </div>
</template>

<script>
import ReviewForm from '@/components/Review/ReviewForm'
import ReviewList from '@/components/Review/ReviewList'

import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'DetailCard',
  components: {
    ReviewForm,
    ReviewList,
  },

  props: {
    movie: {
      type: [Object,],
      default: null,
    }
  },

  methods: {
    reviewPost ( reviewData ) {

      const headers = this.setToken()

      axios({
        url: `${SERVER_URL}/community/${this.movie.id}/review/`,
        method: 'post',
        data: reviewData,
        headers,
      })
        .then( res => {
          const newMovie = { ...this.movie }
          newMovie.reviews.push( res.data )
          this.movie = newMovie
        })
        .catch( err => {
          console.log( err )
        })

    },

    reviewDelete ( reviewData ) {

      const headers = this.setToken()

      axios({
        url: `${SERVER_URL}/community/${this.movie.id}/review/${reviewData.id}/`,
        method: 'delete',
        headers,
      })
        .then( () => {
          const newMovie = { ...this.movie }
          newMovie.reviews = newMovie.reviews.filter( review => {
            return review.id !== reviewData.id
          })
          this.movie = newMovie
        })
        .catch( err => {
          console.log( err )
        })
    },

    reviewPut ( reviewData ) {

      const headers = this.setToken()

      axios({
        url: `${SERVER_URL}/community/${this.movie.id}/review/${reviewData.id}/`,
        method: 'put',
        data: reviewData,
        headers,
      })
        .then( () => {
          const newMovie = { ...this.movie }
          newMovie.reviews = newMovie.reviews.map( review => {
            return review.id === reviewData.id ? reviewData : review
          })
          this.movie = newMovie
        })
        .catch( err => {
          console.log( err )
        })

    },

    setToken () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    close () {
      this.$emit('close-detail')
    },
  },

  computed: {
    poster_path () {
      return this.movie.poster_path ? `https://www.themoviedb.org/t/p/w300${this.movie.poster_path}` : ''
    }
  },
}
</script>

<style>
#detail-window {
  position: absolute;
  left: 10vw;
  /* height: 50vh; */
  width: 80vw;
  /* background-color: rgba(255,255,255,0.7);
  backdrop-filter: blur(3px);
  box-shadow: 0 0 1rem 0 rgba(0, 0, 0, .2); */

  background: rgba( 255, 255, 255, 0.20 );
  box-shadow: 10px 10px 20px rgba( 31, 38, 135, 0.2 );
  backdrop-filter: blur( 20.0px );
  -webkit-backdrop-filter: blur( 20.0px );
  border-radius: 20px;
  border-top: 1px solid rgba( 255, 255, 255, 0.7 );
  border-left: 1px solid rgba( 255, 255, 255, 0.7 );
}

#detail-text {
  color: rgba( 255, 255, 255, 0.6 );
}
</style>