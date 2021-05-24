<template>
  <div v-if="selectedMovie" id="detail-div">
    <img :src="poster_path">
    <span class="mx-2">
      <h2>
        {{ selectedMovie.title }} ({{ release_data }})
        <a @click="addLikedMovie"><i class="fas fa-plus"></i></a>
      </h2>
    </span>
    <p v-if="selectedMovie.overview">{{ selectedMovie.overview }}</p>
    <p v-else>줄거리가 없습니다</p>
  </div>
</template>

<script>
export default {
  name: 'TmdbDetail',
  data: function () {
    return {
      likedMovies: [],
    }
  },
  props: {
    selectedMovie: [String, Object]
  },
  methods: {
    addLikedMovie () {
      const likedMovie = this.selectedMovie
      console.log(likedMovie)

      // 검색 리스트 & 검색창을 초기화
      this.$emit('initialize')
    }
  },
  computed: {
    poster_path () {
      if (this.selectedMovie.poster_path) {
        return `https://www.themoviedb.org/t/p/w300${this.selectedMovie.poster_path}`
      } else {
        return ''
      }
    },
    release_data () {
      return this.selectedMovie.release_date.slice(0, 4)
    }
  }
}
</script>

<style>
.liked {
  color: red; 
}
</style>