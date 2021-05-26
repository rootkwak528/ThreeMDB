<template>  
  <div class="review-item">

    <span class="review-title">{{ review.title }}</span> <br>

    <span class="review-user">{{ review.user }}</span>
    <span class="review-rate">{{ review.rate }}</span> <br>

    <span class="review-content">{{ review.content }}</span> <br>

    <button @click="reviewDelete">삭제하기</button>
    <button @click="reviewUpdate">수정하기</button> <br>

    <hr>

  </div>
</template>

<script>
// import CommentForm from '@/components/Comment/CommentForm'
// import CommentList from '@/components/Comment/CommentList'
// import UpdateReview from '@/components/Review/UpdateReview'

export default {
  name: 'ReviewItem',
  components: {
    // UpdateReview,
    // CommentList,
    // CommentForm,
  },

  props: {
    review: Object,
  },

  methods: {
    reviewDelete () {
      // DetailCard.vue 까지 emit events
      this.$emit('reviewDelete', this.review)
    },

    reviewUpdate () {
      // DetailCard.vue 까지 emit events
      this.$emit('reviewUpdate', this.review)
    },
  }
}
</script>

<style>
.review-item {
  color: rgba( 255, 255, 255, 0.6 );
}
</style>