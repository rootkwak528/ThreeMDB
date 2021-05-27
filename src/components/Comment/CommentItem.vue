<template>  
  <div class="comment-item ms-2">

    <div v-if="!isUpdate">
      <span class="comment-user"><b>- {{ comment.user.username }}</b> : </span>

      <span class="comment-content">
        {{ comment.content }}

        <span v-if="loginUsername === comment.user.username">
          <i @click="toggle" class="far fa-edit community-btn ms-1"></i>
          <i @click="commentDelete" class="far fa-trash-alt community-btn ms-1"></i> 
        </span>
      </span>
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
    loginUsername: String,
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
  height: 1.25rem;
}

.comment-user {
  font-size: 0.7rem;
}

.comment-content {
  font-size: 0.7rem;
}
</style>