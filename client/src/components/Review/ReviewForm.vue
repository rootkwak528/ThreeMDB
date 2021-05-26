<template>
  <div>

    <label class="review-form-label" for="review-title">Title: </label>
    <input 
      name="review-title"
      type="number" 
      v-model.trim="reviewData.title" 
    > <br>

    <label class="review-form-label" for="review-rate">Rate: </label>
    <input 
      name="review-rate"
      type="number" 
      v-model.trim="reviewData.rate" 
    > <br>

    <label class="review-form-label" for="review-content">Content: </label>
    <input 
      name="review-content"
      type="number" 
      v-model.trim="reviewData.content" 
    > <br>

    <button @click="reviewPost(reviewData)" class="detail-button">Submit</button>
    
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
    reviewPost (reviewData) {
      // Django DB POST
      if (reviewData.title && reviewData.content && 0<=reviewData.rate && reviewData.rate<=10) {
        // DetailCard.vue 까지 emit events
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
.review-form-label {
  color: rgba( 255, 255, 255, 0.6 );
}
</style>