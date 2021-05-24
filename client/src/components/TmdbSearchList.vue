<template>
  <div
    id="list-div" 
    class="row row-cols-1 row-cols-md-2 row-cols-lg-3 row-cols-xl-4 g-4 mx-5"
  >
    <TmdbSearchListItem
      v-for="(movie, idx) in movieList"
      :movie=movie
      :key=idx
      @on-click-item="onClickItem"
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
    onClickItem (movie) {
      this.$emit('on-click-item', movie)
    }
  }
}
</script>

<style>

</style>