<template>
  <div class="col">
    <div @click="onClickItem" class="card mb-3 item">
      <div>
        <img  
          v-if="poster_path"
          :src="poster_path"
          alt="movie_poster"
        >
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
        return `https://www.themoviedb.org/t/p/w185${this.movie.poster_path}`
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