<template>

  <div

    id   ="card-list" 
    class="d-flex justify-content-center row g-4 mx-5 pb-5"

  >
    <TmdbSearchItem

      v-for     ="(movie, idx) in movieList"
      :movie    =movie
      :itemIdx  =idx
      :key      =idx
      @clickCard="clickCard"

    />
  </div>

</template>

<script>
import TmdbSearchItem from '@/components/Tmdb/TmdbSearchItem'

export default {
  name: 'TmdbSearchList',
  components: {
    TmdbSearchItem
  },

  props: {
    movieList: [String, Array]
  },

  methods: {
    clickCard ( movie ) {
      // console.log('mid recieve')
      this.$emit('clickCard', movie)
    },
  }
}
</script>

<style>
#card-list {
  margin-top: 2rem;
}
</style>