<template>
  <div>
    <ul>
      <div v-for="(review, idx) in movie.reviews" :key="idx">
        <h3>게시글 {{ idx + 1 }}</h3>
        <h4>평점 : {{ review.rate }}</h4>
        <h4>제목 : {{ review.title }}</h4>
        <p>내용 : {{ review.content }}</p>
        <button @click="deleteReview(review)">삭제하기</button>
        <button @click="onUpdateReview(idx)">수정하기</button>
        <h4>댓글 작성</h4>
        <CreateComment 
          :review="review"
          :movie="movie"
        />
        <CommentList 
          :review="review"
          :movie="movie"
        />
        <!-- 모든 idx에서 켜지는 현상 발생 -->
        <!-- idx 조건 추가 -->
        <div v-if="isUpdateReviewBtnClicked && idx_num_review===idx">
          <UpdateReview 
            :review="review"
            :movie="movie"
            :isUpdateReviewBtnClicked="isUpdateReviewBtnClicked"
          />
        </div>
        <hr>
      </div>
    </ul>
  </div>
</template>

<script>
import CreateComment from '@/components/CreateComment'
import CommentList from '@/components/CommentList'
import UpdateReview from '@/components/UpdateReview'

import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewList',
  data () {
    return {
      isUpdateReviewBtnClicked: false,
      idx_num_review: 0,
    }
  },
  components: {
    UpdateReview,
    CommentList,
    CreateComment,
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
    deleteReview (review) {
      const headers = this.setToken()

      axios({
        url: `${SERVER_URL}/community/${this.movie.id}/review/${review.id}/`,
        method: 'delete',
        headers,
      })
      .then((res) => {
        // 얘도 새로고침 기능 필요
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 리뷰 수정 모달 스위치
    onUpdateReview (idx) {
      this.isUpdateReviewBtnClicked = true
      this.idx_num_review = idx
    }
  }
}
</script>

<style>

</style>