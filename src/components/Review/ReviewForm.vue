<template>
  <div class="review-form pb-2 mb-1">

    <input 
      class="review-input review-title mb-1"
      type="text"
      placeholder="새로운 게시글 제목을 입력해주세요."
      maxlength="40"
      v-model.trim="reviewData.title" 
    >

    <textarea 
      class="review-input-content review-content mb-1"
      placeholder="새로운 게시글 내용을 입력해주세요."
      v-model.trim="reviewData.content"
    ></textarea>

    <div class="d-flex justify-content-between mb-1">
      <input 
        class="review-input"
        type="number"
        min="0"
        max="10"
        v-model.trim="reviewData.rate">

      <span 
        @click="reviewPost(reviewData)" 
        class="review-form-button px-3"> 게시글 등록 </span>
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
      },
    }
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
  },
}
</script>

<style>
.review-form {
  /* background: rgba(255, 255, 255, 0.6); */
  border: 1px solid rgba(255, 255, 255, 0.4);
  border-top-left-radius: 18px;
  border-top-right-radius: 18px;
  padding: 0.5rem;
}

.review-title {
  padding: 0.2rem;
  font-size: 1rem;
}

.review-input-content {
  background: rgba(255, 255, 255, 0.6);
  border: none;
  border-radius: 10px;
  padding: 0.4rem 0.5rem;
  height: 4rem;
  font-size: 0.8rem;
  color: rgba(80, 80, 80, 0.8);
}

.review-input-content:hover {
  background: rgba(255, 255, 255, 0.8);
}

.review-form-button {
  background: rgba(255, 255, 255, 0.6);
  border: none;
  border-radius: 10px;
  padding: 0.4rem 0.5rem;
  height: 43.2px;
  font-size: 0.7rem;
  color: rgba(80, 80, 80, 0.8);
}

.review-form-button:hover {
  background: rgba(255, 255, 255, 0.8);
  font-weight: 600;
  cursor: pointer;
  color: rgba(0, 0, 0, 0.6);
}
</style>