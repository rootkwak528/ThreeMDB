<template>
  <div
    id="card-list" 
    class="d-flex justify-content-center row g-4 mx-5"
  >
    <TmdbSearchListItem
      v-for="(movie, idx) in movieList"
      :movie=movie
      :item_id=idx
      :key=idx
      @clickCard="clickCard"
    />
  </div>
</template>

<script>
import TmdbSearchListItem from '@/components/TmdbSearchListItem'
export default {
  name: 'TmdbSearchList',
  components: {
    TmdbSearchListItem
  },
  props: {
    movieList: [String, Array]
  },
  methods: {
    clickCard (movie) {
      console.log('mid recieve')
      this.$emit('clickCard', movie)
    }
  }
}
</script>

<style>
#card-list {
  margin-top: 2rem;
}
</style>