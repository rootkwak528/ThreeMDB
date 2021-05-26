<template>
  <div>
    movie: {{movie}}<br><br>
    reivew: {{movie.reviews}}
    <ReviewItem
      v-for="(review, idx) in movie.reviews"
      :review="review"
      :key="idx"
    />

  </div>
</template>

<script>
import ReviewItem from '@/components/Review/ReviewItem'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

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