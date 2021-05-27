<template>  
  <div class="comment-item">

    <div v-if="!isUpdate">
      <span class="comment-user">{{ comment.user.username }}: </span>
      <span class="comment-content">{{ comment.content }}</span> <br>

      <button @click="toggle">수정</button>
      <button @click="commentDelete">삭제</button> <br>
    </div>

    <div v-else>
      <label class="comment-form-label" for="comment-content">Content: </label>
      <input 
        name="comment-content"
        type="text" 
        v-model.trim="commentData.content"
      > <br>

      <button @click="commentPut(commentData)">수정</button>
      <button @click="toggle">취소</button> <br>
    </div>

    <hr>

  </div>
</template>

<script>
export default {
  name: 'commentItem',
  data () {
    return {
      commentData: {
        content: '',
      },
      isUpdate: false,
    }
  },

  props: {
    comment: Object,
  },

  methods: {
    commentDelete () {
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentDelete', this.comment )
    },

    commentPut ( commentData ) {
      // DetailCard.vue 까지 emit events
      if ( commentData.content ) {
        this.$emit( 'commentPut', commentData )
        this.toggle()
      }
    },

    toggle () {
      this.commentData = { ...this.comment }
      this.isUpdate = !this.isUpdate
    }
  }
}
</script>

<style>
.comment-item {
  color: rgba( 255, 255, 255, 0.6 );
}
</style>