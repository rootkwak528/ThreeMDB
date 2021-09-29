<template>
  <div class="review-list">
    
    <ReviewItem
      v-for  ="(review, idx) in reviews"
      :review="review"
      :key   ="idx"

      :loginUsername="loginUsername"

      @reviewDelete="reviewDelete"
      @reviewPut   ="reviewPut"

      @commentPost  ="commentPost"
      @commentDelete="commentDelete"
      @commentPut   ="commentPut"
    />
    
  </div>
</template>

<script>
import ReviewItem from '@/components/Review/ReviewItem'

export default {
  name: 'ReviewList',
  components: {
    ReviewItem
  },

  props: {
    reviews: Array,
    loginUsername: String,
  },

  methods: {
    setToken () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    reviewDelete ( reviewData ) {
      // DetailCard.vue 까지 emit events
      this.$emit( 'reviewDelete', reviewData )
    },

    reviewPut ( reviewData ) {
      // DetailCard.vue 까지 emit events
      this.$emit( 'reviewPut', reviewData )
    },

    commentPost ( commentData ) {
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentPost', commentData )
    },

    commentDelete ( commentData ) {
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentDelete', commentData )
    },

    commentPut ( commentData ) {
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentPut', commentData )
    },
  }
}
</script>

<style>
.review-list {
  color: rgba( 255, 255, 255, 0.6 );
}
</style>