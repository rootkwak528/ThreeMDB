<template>
  <div>
    <ul>
      <h5>총 댓글 {{ review.comments.length }}</h5>
      <li v-for="(comment, idx) in review.comments" :key="idx">
        <span>{{ comment.content }}</span>
        <button @click="deleteComment(comment)">X</button>
        <button @click="onUpdateComment">수정</button>
        <div v-if="isUpdateCommentBtnClicked">
          <UpdateComment 
            :comment="comment"
            :review="review"
            :movie="movie"
            :isUpdateCommentBtnClicked="isUpdateCommentBtnClicked"
          />
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import UpdateComment from '@/components/UpdateComment'

import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CommentList',
  data () {
    return {
      isUpdateCommentBtnClicked: false,
    }
  },
  components: {
    UpdateComment,
  },
  props: {
    review: Object,
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
    deleteComment (comment) {
      const headers = this.setToken()
      axios({
        url: `${SERVER_URL}/community/${this.movie.id}/review/${this.review.id}/comment/${comment.id}/`,
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
    },
    onUpdateComment () {
      this.isUpdateCommentBtnClicked = true
    }
  }
}
</script>

<style>

</style>