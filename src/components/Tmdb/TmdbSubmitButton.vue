<template>
  <div class="mx-3">

    <button 
      id="submit-button"
      @click="clickSubmit"
    >
      영화 추천 페이지로 이동!
    </button>

  </div>
</template>

<script>
export default {
  name: 'TmdbSubmitButton',

  methods: {
    clickSubmit () {
      this.$emit('clickSubmit')
    },
  },
}
</script>

<style>
#submit-button {
  text-align: center;
  color: #42b883;
  font-size: 1rem;
  
  width: 546px;
  height: 2.4rem;
  margin-top: 3rem;

  border-style: solid;
  border-radius: 8px;
  border-color: #42b883;
  background: #ffffff;
  /* box-shadow: inset 7px 7px 18px #e3e3e3,
              inset -7px -7px 18px #ffffff; */
}

#submit-button:hover {
  outline: none;
  font-weight: 500;
  color: #ffffff;
  background: #42b883;
  box-shadow: inset 10px 6px 12px #258057;
}
</style>