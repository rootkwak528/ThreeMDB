<template>
  <div class="mx-3">

    <input 
      type="text" 
      @input="onInputText"
      id="input-box"
      placeholder="좋아하는 영화 제목을 입력해주세요."
    >

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
#input-box {
  text-align: center;
  
  width: 546px;
  height: 2.4rem;
  margin-top: 3rem;

  border-style: solid;
  border-radius: 8px;
  border-color: #e7e7e7;
  background: #f7f7f7;
  /* box-shadow: inset 7px 7px 18px #e3e3e3,
              inset -7px -7px 18px #ffffff; */
}

::placeholder {
  font-size: 0.8em;
}

#input-box:focus {
  outline: none;
  /* background-color: black; */
  border-style: solid;
  border-radius: 8px;
  border-color: #aaaaaa;
  box-shadow: 0px 0px 0px #ffffff,
              0px 0px 0px #ffffff;
}
</style>