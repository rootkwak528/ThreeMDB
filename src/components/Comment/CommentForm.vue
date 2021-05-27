<template>
  <div class="d-flex comment-form mt-2">

    <i class="far fa-comment ms-1 me-2"></i>
    <input 
      class="comment-input"
      type="text"
      placeholder="댓글을 입력해주세요."
      v-model.trim="commentData.content"
      @keyup.enter="commentPost(commentData)"
    >

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
.comment-form {
  background: rgba(255, 255, 255, 0.6);
  padding: 0.4rem 0.5rem;
  border-radius: 10px;
  color: rgba(80, 80, 80, 0.65);
}

.comment-form:hover {
  background: rgba(255, 255, 255, 0.8);
}

.comment-input {
  background: transparent;
  border: none;
  width: 100%;
  height: 1rem;
  font-size: 0.8rem;
  color: rgba(80, 80, 80, 0.8);
}
</style>