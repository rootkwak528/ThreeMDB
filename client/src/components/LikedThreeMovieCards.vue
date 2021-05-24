<template>
  <div>
    <div class="row row-cols-3 g-4 mx-5">
      <div class="col">
        <div class="card h-100">
          <div v-if="likedMovies.length >= 1">
            <div class="card-header">
              <h5>{{ likedMovies[0].title }}</h5>
            </div>
            <img :src="poster_path(likedMovies[0])" class="card-img-top" alt="poster-image">
          </div>
          <div v-else>
            <div class="card-header">
              <h3>Movie 1</h3>
            </div>
            <a><i @click="onClickPoster" class="fas fa-plus my-5"></i></a>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card h-100">
          <div v-if="likedMovies.length >= 2">
            <div class="card-header">
              <h5>{{ likedMovies[1].title }}</h5>
            </div>
            <img :src="poster_path(likedMovies[1])" class="card-img-top" alt="poster-image">
          </div>
          <div v-else>
            <div class="card-header">
              <h3>Movie 2</h3>
            </div>
            <a><i @click="onClickPoster" class="fas fa-plus my-5"></i></a>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card h-100">
          <div v-if="likedMovies.length >= 3">
            <div class="card-header">
              <h5>{{ likedMovies[2].title }}</h5>
            </div>
            <img :src="poster_path(likedMovies[2])" class="card-img-top" alt="poster-image">
          </div>
          <div v-else>
            <div class="card-header">
              <h3>Movie 3</h3>
            </div>
            <a><i @click="onClickPoster" class="fas fa-plus my-5"></i></a>
          </div>
        </div>
      </div>
      <button @click="onClick" v-if="likedMovies.length == 3">추천 페이지로!</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LikedThreeMovieCards',
  props: {
    likedMovies: Array,
  },
  methods: {
    onClickPoster () {
      console.log('add liked movie!')
    },
    poster_path (likedMovie) {
      if (likedMovie.poster_path) {
        return `https://www.themoviedb.org/t/p/w185${likedMovie.poster_path}`
      } else {
        return ''
      }
    },
    onClick () {
      const likedMoviesJson = JSON.stringify(this.likedMovies)
      localStorage.clear()
      localStorage.setItem('likedMovies', likedMoviesJson)
      this.$router.push('movies/recommend')
    }
  },
}
</script>

<style>
.card {
  margin: 2px;
}
</style>