<template>
  <div>
    <label class="comment-form-label" for="comment-content">Content: </label>
    <input 
      name="comment-content"
      type="text"
      v-model.trim="commentData.content"
      @keyup.enter="commentPost(commentData)"
    >
    <button @click="commentPost(commentData)">댓글 입력</button>
  </div>
</template>

<script>
export default {
  name: 'CommentForm',
  data () {
    return {
      commentData: {
        content: '',
      },
    }
  },
  
  methods: {
    commentPost ( commentData ) {
      console.log(commentData)
      // Django DB POST
      if ( commentData.content ) {
        // DetailCard.vue 까지 emit events
        this.$emit('commentPost', commentData)
      }

      // initialize
      this.commentData= {
        content: '',
      }
    }
  }
}
</script>

<style>
.comment-form-label {
  color: rgba( 255, 255, 255, 0.6 );
}
</style>