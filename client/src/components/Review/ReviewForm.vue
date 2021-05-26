<template>
  <div>

    <div class="mb-3">
      <label for="review-rate">Rate</label>
      <input type="number" v-model.trim="reviewData.rate" id="review-rate">

      <label for="review-title">Title</label>
      <input type="text" v-model.trim="reviewData.title" id="review-title">
    </div>

    <div class="mb-3">
      <label for="review-content">Content</label>
      <input type="text" v-model.trim="reviewData.content" id="review-content">

      <button @click="createReview(reviewData)" class="detail-button">Submit</button>
    </div>

  </div>
</template>

<script>
export default {
  name: 'ReviewForm',
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
    createReview (reviewData) {
      // Django DB POST
      if (reviewData.title && reviewData.content && 0<=reviewData.rate<=10) {
        this.$emit('reviewPost', reviewData)
      }

      // initialize
      this.reviewData= {
        title: '',
        content: '',
        rate: 0,
      }
    }
  }
}
</script>

<style>

</style>