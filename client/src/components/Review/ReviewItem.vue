<template>
  
  <div>
    <h3>게시글 {{ idx + 1 }}</h3>
    <h4>평점 : {{ review.rate }}</h4>
    <h4>제목 : {{ review.title }}</h4>
    <p>작성자 : {{ review.user }}</p>
    <p>내용 : {{ review.content }}</p>
    <button @click="deleteReview(review)">삭제하기</button>
    <button @click="onUpdateReview(idx)">수정하기</button>
    <h4>댓글 작성</h4>

    <!-- <CreateComment 
      :review="review"
      :movie="movie"
    />

    <CommentList 
      :review="review"
      :movie="movie"
    /> -->
    
    <!-- 모든 idx에서 켜지는 현상 발생 -->
    <!-- idx 조건 추가 -->

    <!-- <div v-if="isUpdateReviewBtnClicked && idx_num_review===idx">
      <UpdateReview 
        :review="review"
        :movie="movie"
        :isUpdateReviewBtnClicked="isUpdateReviewBtnClicked"
      />
    </div> -->

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
  }

}
</script>

<style>

</style>