<template>  
  <div class="review-item">

    <div v-if="!isUpdate">
      <span class="review-title">{{ review.title }}</span> <br>

      <span class="review-user">{{ review.user.username }} / </span>
      <span class="review-rate">{{ review.rate }}</span> <br>

      <span class="review-content">{{ review.content }}</span> <br>

      <button @click="toggleCommentForm">댓글달기</button>
      <button @click="toggle">수정</button>
      <button @click="reviewDelete">삭제</button> <br>
    </div>

    <div v-else>
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

      <button @click="reviewPut(reviewData)">수정</button>
      <button @click="toggle">취소</button> <br>
    </div>

    <div v-if="isCommentForm">
      <CommentForm
        @commentPost="commentPost"
      />
      <button @click="toggleCommentForm">취소</button> <br>
    </div>

    <CommentList
      :comments     ="review.comments"
      @commentDelete="commentDelete"
      @commentPut   ="commentPut"
    />

    <hr>

  </div>
</template>

<script>
import CommentForm from '@/components/Comment/CommentForm'
import CommentList from '@/components/Comment/CommentList'

export default {
  name: 'ReviewItem',
  components: {
    CommentForm,
    CommentList,
  },

  data () {
    return {
      reviewData: {
        title: '',
        content: '',
        rate: 0,
      },
      isUpdate: false,
      isCommentForm: false
    }
  },

  props: {
    review: Object,
  },

  methods: {
    reviewDelete () {
      // DetailCard.vue 까지 emit events
      this.$emit( 'reviewDelete', this.review )
    },

    reviewPut ( reviewData ) {
      // DetailCard.vue 까지 emit events
      if (reviewData.title && reviewData.content && 0<=reviewData.rate && reviewData.rate<=10) {
        this.$emit( 'reviewPut', reviewData )
        this.toggle()
      }
    },

    commentPost ( commentData ) {
      commentData = {
        ...commentData,
        review: this.review.id
      }
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentPost', commentData )
    },

    commentDelete ( commentData ) {
      commentData = {
        ...commentData,
        review: this.review.id
      }
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentDelete', commentData )
    },

    commentPut ( commentData ) {
      commentData = {
        ...commentData,
        review: this.review.id
      }
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentPut', commentData )
    },

    toggle () {
      this.reviewData = { ...this.review }
      this.isUpdate = !this.isUpdate
    },

    toggleCommentForm () {
      this.isCommentForm = !this.isCommentForm
    },
  }
}
</script>

<style>
.review-item {
  color: rgba( 255, 255, 255, 0.6 );
}
</style>