<template>  
  <div class="review-item text-start pt-1 pb-2">
    <div class="mb-1">

      <!-- if read -->
      <div v-if="!isUpdate">
        <div class="d-flex justify-content-between align-items-end">
          <div>
            <span class="review-title"><b>{{ review.title }}</b></span>
          </div>

          <span class="review-body review-date">{{ review.created_at.slice( 0, 10 ) }}</span>
        </div>

        <div class="d-flex justify-content-between align-items-end">
          <span class="review-body review-rate">{{ review.rate }}</span> <br>

          <span class="review-body review-user">
            by <b>{{ review.user.username }}</b>
            
            <span v-if="loginUsername === review.user.username">
              <i @click="toggle" class="far fa-edit community-btn ms-1"></i>
              <i @click="reviewDelete" class="far fa-trash-alt community-btn ms-1"></i> 
            </span>
          </span>
        </div>

        <span class="review-body review-content">{{ review.content }}</span> <br>

        <div>
          <CommentForm
            @commentPost="commentPost"
          />
        </div>
      </div>

      <!-- else update -->
      <div v-else>
        <div class="d-flex justify-content-between align-items-end mb-1">
          <!-- <div class="review-form">
          </div> -->
          <input 
            type="text" 
            class="review-input review-title" 
            v-model.trim="reviewData.title">
        </div>

        <div class="d-flex justify-content-between align-items-start mb-1">
          <!-- <div class="review-form">
          </div> -->
            <input 
              type="number" 
              class="review-input" 
              v-model.trim="reviewData.rate">

          <span class="review-body review-user">
            by <b>{{ review.user.username }}</b>
            
            <span v-if="loginUsername === review.user.username">
              <i @click="reviewPut(reviewData)" class="far fa-edit community-btn ms-1"></i>
            </span>
          </span>
        </div>

        <!-- <div class="review-form">
        </div> -->
          <input 
            type="text" 
            class="review-input review-content" 
            v-model.trim="reviewData.content"> <br>
      </div>
    </div>

    <CommentList
      :loginUsername="loginUsername"

      :comments     ="review.comments"
      @commentDelete="commentDelete"
      @commentPut   ="commentPut"
    />
    
  </div>
</template>

<script>
import CommentForm from '@/components/Comment/CommentForm'
import CommentList from '@/components/Comment/CommentList'

export default {
  name: 'ReviewItem',
  components: {
    CommentForm,
    CommentList,
  },

  data () {
    return {
      reviewData: {
        title: '',
        content: '',
        rate: 0,
      },
      isUpdate: false,
      isCommentForm: false
    }
  },

  props: {
    review: Object,
    loginUsername: String,
  },

  methods: {
    reviewDelete () {
      // DetailCard.vue 까지 emit events
      this.$emit( 'reviewDelete', this.review )
    },

    reviewPut ( reviewData ) {
      console.log(reviewData)
      // DetailCard.vue 까지 emit events
      if (reviewData.title && reviewData.content && 0<=reviewData.rate && reviewData.rate<=10) {
        this.$emit( 'reviewPut', reviewData )
        this.toggle()
      }
    },

    commentPost ( commentData ) {
      commentData = {
        ...commentData,
        review: this.review.id
      }
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentPost', commentData )
    },

    commentDelete ( commentData ) {
      commentData = {
        ...commentData,
        review: this.review.id
      }
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentDelete', commentData )
    },

    commentPut ( commentData ) {
      commentData = {
        ...commentData,
        review: this.review.id
      }
      // DetailCard.vue 까지 emit events
      this.$emit( 'commentPut', commentData )
    },

    toggle () {
      this.reviewData = { ...this.review }
      this.isUpdate = !this.isUpdate
    },

    toggleCommentForm () {
      this.isCommentForm = !this.isCommentForm
    },
  },
}
</script>

<style>
.review-item {
  color: rgba( 255, 255, 255, 0.6 );
  border-bottom: 1px solid rgba( 255, 255, 255, 0.4 );
}

.review-title {
  padding: 0.2rem;
  font-size: 1rem;
  border-radius: 10px;
  width: 100%;
}

.review-body  {
  padding: 0.2rem;
  font-size: 0.8rem;
  border-radius: 10px;
}

.review-content {
  width: 100%;
}

.review-input {
  background: rgba(255, 255, 255, 0.6);
  border: none;
  border-radius: 10px;
  padding: 0.4rem 0.5rem;
  height: 43.2px;
  font-size: 0.8rem;
  color: rgba(80, 80, 80, 0.8);
}

.review-input:hover {
  background: rgba(255, 255, 255, 0.8);
}

.community-btn:hover {
  cursor: pointer;
  color: rgba(255, 255, 255, 1);
}
</style>