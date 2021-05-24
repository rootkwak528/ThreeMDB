<template>
  <div>
    <div class="row row-cols-3 g-4 mx-5">
      <div class="col">
        <div class="card h-100">
          <div class="card-header">
            Movie 1
          </div>
          <div v-if="movieCnt">
            <img src="#" class="card-img-top" alt="poster-image">
          </div>
          <div v-else>
            <a><i @click="onClickPoster" class="fas fa-plus my-5"></i></a>
          </div>
          <div class="card-body">
            <h5 class="card-title">movieItem.title</h5>
            <p class="card-text">movieItem.overview</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card h-100">
          <div class="card-header">
            Movie 2
          </div>
          <!-- <div v-if="likedMovies.length >= 2"></div> -->
          <div v-if="movieCnt">
            <img src="#" class="card-img-top" alt="poster-image">
          </div>
          <div v-else>
            <a><i @click="onClickPoster" class="fas fa-plus my-5"></i></a>
          </div>
          <div class="card-body">
            <h5 class="card-title">movieItem.title</h5>
            <p class="card-text">movieItem.overview</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card h-100">
          <div class="card-header">
            Movie 3
          </div>
          <div v-if="movieCnt">
            <img src="#" class="card-img-top" alt="poster-image">
          </div>
          <div v-else>
            <a><i @click="onClickPoster" class="fas fa-plus my-5"></i></a>
          </div>
          <div class="card-body">
            <h5 class="card-title">movieItem.title</h5>
            <p class="card-text">movieItem.overview</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LikedThreeMovieCards',
  data () {
    return {
      movieCnt: 0,
    }
  },
  methods: {
    onClickPoster () {
      console.log('add liked movie!')
    }
  }
}
</script>

<style>
.card {
  margin: 2px;
}
</style>