<template>
  <div>
    <ul>
      <h5>총 댓글 {{ review.comments.length }}</h5>
      <li v-for="(comment, idx) in review.comments" :key="idx">
        <span>{{ comment.content }}</span>
        <button @click="deleteComment(comment)">X</button>
        <button @click="onUpdateComment(idx)">수정</button>
        <!-- 모든 idx에서 켜지는 현상 발생 -->
        <!-- idx 조건 추가 -->
        <div v-if="isUpdateCommentBtnClicked && idx_num_comment===idx">
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
      idx_num_comment: 0,
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
    // 댓글 수정 모달 스위치
    onUpdateComment (idx) {
      this.isUpdateCommentBtnClicked = true
      this.idx_num_comment = idx
    }
  }
}
</script>

<style>

</style>