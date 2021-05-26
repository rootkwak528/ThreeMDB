<template>
  <div id="index-head" class="d-flex flex-column align-items-center">

    <span id="index-title">
      <span class="mx-1">&#127916;</span>당신이 좋아하는 영화
      <span class="mx-1">&#127916;</span>
    </span>

    <div class="d-flex justify-content-center align-items-center g-4 mx-5" id="index-head-body">

      <TmdbLikedItem

        v-for          ="(likedMovie, idx) in likedMovies"
        :likedMovie    =likedMovie
        :itemIdx       =idx
        :key           =idx
        @clickLikedCard="clickLikedCard"

      />
    </div>

  </div>
</template>

<script>
import TmdbLikedItem from '@/components/TmdbLikedItem'

export default {
  name: 'TmdbLikedList',
  components: {
    TmdbLikedItem,
  },
  props: {
    likedMovies: Array,
  },

  methods: {
    clickLikedCard ( likedMovie ) {
      this.$emit('clickLikedCard', likedMovie)
    },
  },
}
</script>

<style>
#index-head {
  margin-top: 5vh;
}

#index-title {
  position: absolute;

  font-size: 0.8rem;
  
  padding: 0 0.5rem;

  background-color: #ffffff;
}

#index-head-body {
  width: 646px;
  height: 325px;
  margin-top: 0.4rem;

  border-radius: 8px;
  background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' rx='8' ry='8' stroke='%23333' stroke-width='1' stroke-dasharray='12' stroke-dashoffset='0' stroke-linecap='square'/%3e%3c/svg%3e");
}
</style>