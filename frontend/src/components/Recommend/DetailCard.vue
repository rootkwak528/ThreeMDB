<template>
  <div id="detail-window">
    <div class="container">
      <div class="row">

        <div class="col-6">

          <img
            v-if="poster_path"
            :src="poster_path"
            alt="movie_poster"
          > <br>
          
          <div class="detail-header">
            <span class="detail-title"><b>{{ movie.title }}</b></span> <br>
            <span class="detail-release-date">{{ movie.release_date }}</span> <br>
          </div>

          <div class="detail-header">
            <span class="detail-rate"><b><i class="fas fa-star"></i> {{ averageRate }}</b></span>
          </div>

          <div class="detail-body text-start">
            <span class="detail-overview">{{ movie.overview }}</span> <br>
          </div>
        </div>

        <div class="col-6">
          
          <div class="d-flex justify-content-end">
            <span class="community-btn" id="close-btn" @click="close"><i class="fas fa-times"></i></span>
          </div>
          
          <ReviewForm 
            @reviewPost="reviewPost"
          />

          <ReviewList 
            :loginUsername="loginUsername"
            
            :reviews      ="movie.reviews"
            @reviewDelete ="reviewDelete"
            @reviewPut    ="reviewPut"

            @commentPost  ="commentPost"
            @commentDelete="commentDelete"
            @commentPut   ="commentPut"
          />

        </div>

      </div>
    </div>
  </div>
</template>

<script>
import ReviewForm from '@/components/Review/ReviewForm'
import ReviewList from '@/components/Review/ReviewList'

import axios from 'axios'
import jwt_decode from 'jwt-decode'
import { mapState } from 'vuex'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'DetailCard',
  components: {
    ReviewForm,
    ReviewList,
  },
  
  data () {
    return {
      movie: {},
    }
  },

  computed: {
    ...mapState([
      'movieDetail'
    ]),

    poster_path () {
      return this.movie.poster_path ? `https://www.themoviedb.org/t/p/w300${this.movie.poster_path}` : ''
    },

    authToken () {
      return localStorage.getItem('jwt')
    },

    loginUsername () {
      const decode = jwt_decode(this.authToken)
      return decode ? decode.username : 'anonymous_User'
    },

    averageRate () {
      let rateSum = 0, rateCount = 0
      this.movieDetail.reviews.forEach( review => {
        rateSum += review.rate
        rateCount += 1
      })
      return rateCount ? (rateSum / rateCount).toFixed(2) : 0
    },
  },

  mounted () {
    // this.movie 는 vuejs 에서만 바뀌는 데이터로, DB 를 **미믹한다.**
    // 미믹 없이 바로 prop 을 수정하면, Vue warn 이 발생한다.
    this.movie = { ...this.movieDetail }

    console.log('DetailCard.vue mounted()', this.movieDetail)
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
        url: `${SERVER_URL}/community/review/${reviewData.id}/`,
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
        url: `${SERVER_URL}/community/review/${reviewData.id}/`,
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

    commentPost ( commentData ) {

      const headers = this.setToken()

      axios({
        url: `${SERVER_URL}/community/review/${commentData.review}/comment/`,
        method: 'post',
        data: commentData,
        headers,
      })
        .then( res => {
          const newMovie = { ...this.movie }
          newMovie.reviews = newMovie.reviews.map( review => {

            if ( review.id === commentData.review ) {

              const newReview = { ...review }
              newReview.comments.push(res.data)
              return newReview

            } else {
              return review
            }
          })
          this.movie = newMovie
          
        })
        .catch( err => {
          console.log( err )
        })

    },

    commentDelete ( commentData ) {

      const headers = this.setToken()

      axios({
        url: `${SERVER_URL}/community/review/${commentData.review}/comment/${commentData.id}/`,
        method: 'delete',
        headers,
      })
        .then( () => {
          const newMovie = { ...this.movie }
          newMovie.reviews = newMovie.reviews.map( review => {

            if ( review.id === commentData.review ) {

              const newReview = { ...review }
              newReview.comments = newReview.comments.filter( comment => {
                return comment.id !== commentData.id
              })
              return newReview

            } else {
              return review
            }
          })
          this.movie = newMovie
          
        })
        .catch( err => {
          console.log( err )
        })

    },

    commentPut ( commentData ) {

      const headers = this.setToken()

      axios({
        url: `${SERVER_URL}/community/review/${commentData.review}/comment/${commentData.id}/`,
        method: 'put',
        data: commentData,
        headers,
      })
        .then( () => {
          const newMovie = { ...this.movie }
          newMovie.reviews = newMovie.reviews.map( review => {

            if ( review.id === commentData.review ) {

              const newReview = { ...review }
              newReview.comments = newReview.comments.map( comment => {
                return comment.id === commentData.id ? commentData : comment
              })
              return newReview

            } else {
              return review
            }
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
}
</script>

<style>
#detail-window {
  color: rgba( 255, 255, 255, 0.6 );

  position: absolute;
  
  top: 10vh;

  left: 10vw;
  width: 80vw;

  margin-bottom: 10vh;
  /* background-color: rgba(255,255,255,0.7);
  backdrop-filter: blur(3px);
  box-shadow: 0 0 1rem 0 rgba(0, 0, 0, .2); */

  padding: 3rem;

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

.detail-title {
  font-size: 1.5rem;
}

.detail-header {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.detail-rate {
  color: rgba(255, 215, 0, 0.8);
  font-size: 1.2rem;
}

.detail-overview {
  font-size: 0.8rem;
}

#close-btn {
  padding: 0;
  margin: 0;
  margin-bottom: 1rem;
  font-size: 2rem;
}
</style>