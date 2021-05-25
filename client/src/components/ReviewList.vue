<template>
  <div>
    <ul>
      <div v-for="(review, idx) in movie.reviews" :key="idx">
        <h3>게시글 {{ idx + 1 }}</h3>
        <h4>평점 : {{ review.rate }}</h4>
        <h4>제목 : {{ review.title }}</h4>
        <p>내용 : {{ review.content }}</p>
        <button @click="deleteReview(review)">삭제하기</button>
        <hr>
      </div>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewList',
  props: {
    movie: Object,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteReview (review) {
      const headers = this.setToken()

      axios({
        url: `${SERVER_URL}/community/${this.movie.id}/review/${review.id}/delete/`,
        method: 'delete',
        headers,
      })
      .then((res) => {
        // 얘도 새로고침 기능 필요
        console.log('여기',res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>