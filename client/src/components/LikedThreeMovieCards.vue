<template>
  <div id="index-head" class="d-flex flex-column align-items-center">
    <span id="index-title">
      <span class="mx-1">&#127916;</span>
      당신이 좋아하는 영화
      <span class="mx-1">&#127916;</span>
    </span>

    <div class="d-flex justify-content-center align-items-center g-4 mx-5" id="index-head-body">
      <div class="my-card d-flex flex-column justify-content-center">
        <div v-if="likedMovies.length >= 1">
          <img :src="poster_path(likedMovies[0])" class="card-img-top" alt="poster-image" height="300">
        </div>
        <div v-else>
          <span>
            카드가<br/>
            비어있습니다.<br/>
          </span>
          <!-- <a><i @click="onClickPoster" class="fas fa-plus my-5"></i></a> -->
        </div>
      </div>

      <div class="my-card d-flex flex-column justify-content-center">
        <div v-if="likedMovies.length >= 2">
          <img :src="poster_path(likedMovies[1])" class="card-img-top" alt="poster-image">
        </div>
        <div v-else>
          <span>
            카드가<br/>
            비어있습니다.<br/>
          </span>
          <!-- <a><i @click="onClickPoster" class="fas fa-plus my-5"></i></a> -->
        </div>
      </div>

      <div class="my-card d-flex flex-column justify-content-center">
        <div v-if="likedMovies.length >= 3">
          <img :src="poster_path(likedMovies[2])" class="card-img-top" alt="poster-image">
        </div>
        <div v-else>
          <span>
            카드가<br/>
            비어있습니다.<br/>
          </span>
          <!-- <a><i @click="onClickPoster" class="fas fa-plus my-5"></i></a> -->
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
      localStorage.setItem('likedMovies', likedMoviesJson)
      this.$router.push('movies/recommend')
    }
  },
}
</script>

<style>
#index-head {
  margin-top: 5vh;
}

#index-title {
  position: absolute;

  font-size: 0.8rem;
  
  padding: 0 0.5rem;

  background-color: #ffffff;
}

#index-head-body {
  width: 646px;
  height: 325px;
  margin-top: 0.4rem;

  border-radius: 8px;
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' rx='8' ry='8' stroke='%23333' stroke-width='1' stroke-dasharray='12' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e");
}

.my-card {
  font-size: 0.5rem;

  width: 150px;
  height: 225px;
  margin: 1rem 1rem;
  
  border-radius: 8px;
  background: #ffffff;
  box-shadow: inset 7px 7px 18px #e3e3e3,
              inset -7px -7px 18px #ffffff;
}
</style>