<template>

  <div 

    :id   ="cardId"
    :class="{ card: !likedMovie, 
              cardImage: likedMovie }"
    class ="d-flex justify-content-center align-items-center"
    @click="removeCard(likedMovie)"

  >
    <span class="liked-tooltip-text"><b>{{ likedMovie.title }}</b></span>

    <span v-if="!posterPath">
      카드가<br/>
      비어있습니다.<br/>
    </span>

  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TmdbLikedItem',
  props: {
    likedMovie: [Object, String],
    itemIdx: Number,
  },
  
  methods: {
    ...mapActions([
      'removeCard',
    ])
  },

  updated () {
    const card = document.querySelector(`#${ this.cardId }`)
    card.style.backgroundImage = this.posterPath ? `url(${ this.posterPath })` : 'none'
  },

  computed: {
    posterPath () {
      return this.likedMovie.poster_path ? `https://www.themoviedb.org/t/p/w185${ this.likedMovie.poster_path }` : ''
    },

    cardId () {
      return `liked-card-${ this.itemIdx }`
    },
  },
}
</script>

<style>
/* 
  .card 와 .cardImage 의 스타일은 TmdbSearchItem.vue 참고
*/

/* Tooltip text */
.cardImage .liked-tooltip-text {
  display: inline-block;
  font-size: 0.8rem;
  visibility: hidden;
  background-color: beige;
  box-shadow: 4px 4px 8px #000000;
  text-align: center;
  padding: 5px 10px;
  border-radius: 6px;
 
  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 10;
}

/* Show the tooltip text when you mouse over the tooltip container */
.cardImage:hover .liked-tooltip-text {
  visibility: visible;
  top: 105%;
}
</style>