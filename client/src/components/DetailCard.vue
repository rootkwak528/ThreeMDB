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
    <div id="detail-text">
      <h4>{{ movie.title }}</h4>
      <p>{{ movie.overview }}</p>
    </div>
    <ReviewList />
    <CreateReview 
      :movieData="movieData"
    />
  </div>
</template>

<script>
import CreateReview from '@/components/CreateReview'
import ReviewList from '@/components/ReviewList'
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'DetailCard',
  data () {
    return {
      movieData: '',
    }
  },
  components: {
    CreateReview,
    ReviewList,
  },
  props: {
    movie: {
      type: [Object,],
      default: null,
    }
  },
  methods: {
    setToken () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    close () {
      this.$emit('close-detail')
    }
  },
  computed: {
    poster_path () {
      if (this.movie.poster_path) {
        return `https://www.themoviedb.org/t/p/w300${this.movie.poster_path}`
      } else {
        return ''
      }
    }
  },
  created () {
    axios({
      url: `${SERVER_URL}/movies/`,
      method: 'post',
      data: this.movie,
    })
    .then((res) => {
      this.movieData = res
      console.log(this.movieData)
    })
    .catch((err) => {
      console.log(err)
    })
  }
}
</script>

<style>
#detail-window {
  position: absolute;
  top: 30vh;
  left: 20vw;
  /* height: 50vh; */
  width: 60vw;
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