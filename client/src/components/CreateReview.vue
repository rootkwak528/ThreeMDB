<template>
  <div>
    <form>
      <div class="mb-3">
        <label for="review-title" class="form-label">Title</label>
        <input type="text" v-model.trim="title" class="form-control" id="review-title">
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">Content</label>
        <input type="text" v-model.trim="content" class="form-control" id="content">
      </div>
      <button @click="createReview" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateReview',
  data () {
    return {
      title: '',
      content: '',
    }
  },
  props: {
    movieData: Object
  },
  methods: {
    setToken () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview () {
      const headers = this.setToken()

      const ReviewItem = {
        title: this.title,
        content: this.content
      }
      if (ReviewItem.title && ReviewItem.content) {
        axios({
          url: `${SERVER_URL}/community/${this.movieData.data.id}/review/`,
          method: 'post',
          data: ReviewItem,
          headers,
        })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      }
      this.title = ''
      this.content = ''
    }
  }
}
</script>

<style>

</style>