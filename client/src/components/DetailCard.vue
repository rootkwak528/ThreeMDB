<template>
  <div id="detail">
    <div class="col">
      <img  
        v-if="poster_path"
        :src="poster_path"
        alt="movie_poster"
      >
      <button class="position-absolute top-0 start-100" @click="close">x</button>
    </div>
    <div>
      <h4>{{ movie.title }}</h4>
      <p>{{ movie.overview }}</p>
    </div>
    <CreateReview 
      :movieData="movieData"
    />
  </div>
</template>

<script>
import CreateReview from '@/components/CreateReview'
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
    })
    .catch((err) => {
      console.log(err)
    })
  }
}
</script>

<style>
#detail {
  position: absolute;
  top: 30vh;
  left: 20vw;
  /* height: 50vh; */
  width: 60vw;
  background-color: rgba(255,255,255,0.7);
  backdrop-filter: blur(3px);
  box-shadow: 0 0 1rem 0 rgba(0, 0, 0, .2);
}
</style>