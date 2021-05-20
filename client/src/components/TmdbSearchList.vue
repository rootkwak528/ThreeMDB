<template>
  <div>
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