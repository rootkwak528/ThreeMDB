<template>
  <div class="col">
    <div @click="onClickItem" class="card mb-3 item">
      <div class="row g-0">
        <div class="col-md-4">
          <img  
            v-if="poster_path"
            :src="poster_path"
            alt="movie_poster"
          >
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <h3 class="card-title">{{ movie.title }}</h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TmdbSearchListItem',
  props: {
    movie: Object
  },
  methods: {
    onClickItem () {
      this.$emit('on-click-item', this.movie)
    }
  },
  computed: {
    poster_path () {
      if (this.movie.poster_path) {
        return `https://www.themoviedb.org/t/p/w92${this.movie.poster_path}`
      } else {
        return ''
      }
    }
  }
}
</script>

<style>
  .item {
    cursor: pointer;
  }

  .item:hover {
    background: #eee;
  }
</style>