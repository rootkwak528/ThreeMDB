<template>
  <div>
    {{ likedMovies[0] }}
    <p>hello</p>
  </div>
</template>

<script>
export default {
  name: 'MovieRecommend',
  data () {
    return {
      likedMovies: [],
    }
  },
  mounted () {
    const likedMoviesJson = localStorage.getItem('likedMovies')
    this.likedMovies = JSON.parse(likedMoviesJson)
  }
}
</script>

<style>

</style>