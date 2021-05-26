<template>
  <div class="review-list">

    <br><br>movie: {{movie}}<br><br>
    
    <ReviewItem
      v-for        ="(review, idx) in movie.reviews"
      :review      ="review"
      :key         ="idx"
      @reviewDelete="reviewDelete"
      @reviewPut   ="reviewPut"
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

  data () {
    return {
      isUpdateReviewBtnClicked: false,
      idx_num_review: 0,
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

    reviewDelete ( reviewData ) {
      // DetailCard.vue 까지 emit events
      this.$emit( 'reviewDelete', reviewData )
    },

    reviewPut ( reviewData ) {
      // DetailCard.vue 까지 emit events
      this.$emit( 'reviewPut', reviewData )
    },
  }
}
</script>

<style>
.review-list {
  color: rgba( 255, 255, 255, 0.6 );
}
</style>