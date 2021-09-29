<template>

  <div
    id   ="card-list" 
    class="d-flex justify-content-center row g-4 mx-5 pb-5"
  >
    <TmdbSearchItem
      v-for   ="(movie, idx) in searchResults"
      :movie  =movie
      :itemIdx=idx
      :key    =idx
    />
  </div>

</template>

<script>
import TmdbSearchItem from '@/components/TmdbSearch/TmdbSearchItem'
import { mapState } from 'vuex'

export default {
  name: 'TmdbSearchList',
  components: {
    TmdbSearchItem
  },

  computed: {
    ...mapState([
      'searchResults',
    ])
  },
}
</script>

<style>
#card-list {
  margin-top: 2rem;
}
</style>