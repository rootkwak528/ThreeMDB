<template>
  <div>
    <input type="text" v-model.trim="content" @keypress.enter="createComment">
    <button @click="createComment">+</button>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateComment',
  data () {
    return {
      content: '',
    }
  },
  props: {
    movie: Object,
    review: Object,
  },
  methods: {
    setToken () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createComment () {
      const headers = this.setToken()

      const commentItem = {
        content: this.content,
      }
      if (commentItem.content) {
        axios({
          url: `${SERVER_URL}/community/${this.movie.id}/review/${this.review.id}/comment/`,
          method: 'post',
          data: commentItem,
          headers,
        })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      }
      this.content = ''
    }
  }
}
</script>

<style>

</style>