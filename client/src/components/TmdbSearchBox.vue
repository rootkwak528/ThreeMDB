<template>
  <div class="mx-3">
    <input 
      type="text" 
      @input="onInputText"
      id="input-box"
    >
    <!-- <button
      @click="onResetText"
    >
      reset
    </button> -->
    <hr>
    
  </div>
</template>

<script>
export default {
  name: 'TmdbSearchBox',
  props: {
    searchInit: Boolean
  },
  methods: {
    onInputText (event) {
      const searchKeyword = event.target.value.trim()
      if (searchKeyword) {
        this.$emit('tmdb-text-input', searchKeyword)
      }
    },
    onResetText () {
      const inputBox = document.querySelector('#input-box')
      inputBox.value = ''
    }
  },
  watch: {
    searchInit (val) {
      if (val) {
        this.onResetText()
        this.$emit('textResetComplete')
      }
    }
  }
}
</script>

<style>

</style>