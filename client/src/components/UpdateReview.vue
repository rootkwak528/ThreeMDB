<template>
  <div>
    <div class="mb-3">
      <label for="update-review-title">Title</label>
      <input type="text" v-model.trim="updateReviewData.title" id="update-review-title">
    </div>
    <div class="mb-3">
      <label for="update-review-content">Content</label>
      <input type="text" v-model.trim="updateReviewData.content" id="update-review-content">
    </div>
    <div class="mb-3">
      <label for="update-review-rate">Rate</label>
      <input type="number" v-model.trim="updateReviewData.rate" id="update-review-rate">
    </div>
    <button @click="updateReview(updateReviewData, review)">Submit</button>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'UpdateReview',
  data () {
    return {
      updateReviewData: {
        title: '',
        content: '',
        rate: 0,
      }
    }
  },
  props: {
    review: Object,
    movie: Object
  },
  methods: {
    setToken () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    updateReview (updateReviewData, review) {
      const headers = this.setToken()
      
      if (updateReviewData.title && updateReviewData.content && updateReviewData.rate) {
        axios({
          url: `${SERVER_URL}/community/${this.movie.id}/review/${review.id}/`,
          method: 'put',
          data: updateReviewData,
          headers,
        })
        .then((res) => {
          this.movie.reviews.push(res)
        })
        .catch((err) => {
          console.log(err)
        })
      }
      this.updateReviewData.title = ''
      this.updateReviewData.content = ''
      this.updateReviewData.rate = 0
    }
  }
}
</script>

<style>

</style>