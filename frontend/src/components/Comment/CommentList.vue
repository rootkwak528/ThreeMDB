<template>
  <div class="comment-list">

    <CommentItem
      v-for   ="(comment, idx) in comments"
      :comment="comment"
      :key    ="idx"

      :loginUsername="loginUsername"

      @commentDelete="commentDelete"
      @commentPut   ="commentPut"
    />
    
  </div>
</template>

<script>
import CommentItem from '@/components/Comment/CommentItem'

export default {
  name: 'CommentList',
  components: {
    CommentItem
  },

  props: {
    comments: Array,
    loginUsername: String,
  },

  methods: {
    setToken () {
      const token = localStorage.getItem('jwt')

      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    commentDelete ( commentData ) {
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentDelete', commentData )
    },

    commentPut ( commentData ) {
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentPut', commentData )
    },
  }
}
</script>

<style>
.review-list {
  color: rgba( 255, 255, 255, 0.6 );
}
</style>