<template>
  <div>
    <div>
      <input type="text" v-model.trim="content" @keypress.enter="updateComment">
      <button @click="updateComment">댓글 수정</button>
    </div>
  </div>
</template>

<script>
import axios from'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'UpdateComment',
  data () {
    return {
      content: '',
    }
  },
  props: {
    comment: Object,
    review: Object,
    movie: Object,
    isUpdateCommentBtnClicked: Boolean
  },
  methods: {
    setToken () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    updateComment () {
      const headers = this.setToken()

      const commentItem = {
        content: this.content,
      }
      if (commentItem.content) {
        axios({
          url: `${SERVER_URL}/community/${this.movie.id}/review/${this.review.id}/comment/${this.comment.id}/`,
          method: 'put',
          data: commentItem,
          headers,
        })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      }
      this.content = ''
    }
  }
}
</script>

<style>

</style>