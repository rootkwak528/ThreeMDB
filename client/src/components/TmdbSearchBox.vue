<template>
  <div>
    <input 
      type="text" 
      @input="onInputText" 
      @keyup.enter="onResetText"
    >
    <hr>
  </div>
</template>

<script>
export default {
  name: 'TmdbSearchBox',
  methods: {
    onInputText (event) {
      const searchKeyword = event.target.value.trim()
      if (searchKeyword) {
        this.$emit('tmdb-text-input', searchKeyword)
      }
    },
    onResetText (event) {
      event.target.value = ''
    }
  }
}
</script>

<style>

</style>