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
#card-list {
  margin-top: 2rem;
}
</style>