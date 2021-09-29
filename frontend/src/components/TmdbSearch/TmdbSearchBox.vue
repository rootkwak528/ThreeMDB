<template>
  <div class="mx-3">

    <input 
      id         ="input-box"
      type       ="text"
      v-model    ="tmpSearchInput"
      placeholder="좋아하는 영화 제목을 입력해주세요."
      @input     ="setSearchInput(tmpSearchInput)"
    >

  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'TmdbSearchBox',

  data () {
    return {
      tmpSearchInput: '',
    }
  },

  computed: {
    ...mapState([
      'searchInput',
    ])
  },

  methods: {
    ...mapActions([
      'setSearchInput',
    ]),
  },

  watch: {
    searchInput (val) {
      if (!val) {
        this.tmpSearchInput = val
      }
    },
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