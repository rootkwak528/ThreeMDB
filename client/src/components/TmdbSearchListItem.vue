<template>
  <li @click="onClickItem" class="item">
    <img  
      v-if="poster_path"
      :src="poster_path"
      alt="movie_poster"
    >
    {{ movie.title }}
  </li>
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