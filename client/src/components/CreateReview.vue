<template>
  <div>
    <div class="mb-3">
      <label for="review-title">Title</label>
      <input type="text" v-model.trim="reviewData.title" id="review-title">
    </div>
    <div class="mb-3">
      <label for="review-content">Content</label>
      <input type="text" v-model.trim="reviewData.content" id="review-content">
    </div>
    <div class="mb-3">
      <label for="review-rate">Rate</label>
      <input type="number" v-model.trim="reviewData.rate" id="review-rate">
    </div>
    <button @click="createReview(reviewData)" class="detail-button">Submit</button>
  </div>
</template>

<script>
import axios from'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateReview',
  data () {
    return {
      reviewData: {
        title: '',
        content: '',
        rate: 0,
      }
    }
  },
  props: {
    movie: Object,
  },
  methods: {
    setToken () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createReview (reviewData) {
      const headers = this.setToken()
      
      if (reviewData.title && reviewData.content && reviewData.rate) {
        console.log(Date.now(), 'client request')
        console.log(reviewData)
        console.log(this.movie)
        console.log('movie:', this.movie.id)
        console.log(`${SERVER_URL}/community/${this.movie.id}/review/`)
        console.log(headers)
        axios({
          url: `${SERVER_URL}/community/${this.movie.id}/review/`,
          method: 'post',
          data: reviewData,
          headers,
        })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      }
      this.reviewData.title = ''
      this.reviewData.content = ''
      this.reviewData.rate = 0
    }
  }
}
</script>

<style>
.detail-button {
  align-items: center;
  background: linear-gradient(-45deg, rgba(0,0,0,0.22), rgba(255,255,255,0.25));
  border-radius: 50px;
  height: 200px;
  justify-content: center;
  width: 100%;
  box-shadow: 
    12px 12px 16px 0 rgba(0, 0, 0, 0.25),
    -8px -8px 12px 0 rgba(255, 255, 255, 0.3);
}
</style>