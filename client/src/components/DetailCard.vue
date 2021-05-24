<template>
  <div id="detail">
    <h1>detail</h1>
    <h2>{{ movie.id }}</h2>
    <h2>{{ movie.title }}</h2>
    <p>{{ movie.overview }}</p>
    {{movie}}
    <button @click="close">x</button>
  </div>
</template>

<script>
export default {
  name: 'DetailCard',
  props: {
    movie: {
      type: [Object,],
      default: null,
    }
  },
  methods: {
    close () {
      this.$emit('close-detail')
    }
  },
}
</script>

<style>
#detail {
  position: absolute;
  top: 40vh;
  left: 40vw;
  height: 30vh;
  width: 30vw;
  background-color: aquamarine;
}
</style>