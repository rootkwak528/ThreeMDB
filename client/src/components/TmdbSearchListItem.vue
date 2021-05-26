<template>

  <div 

    :id   ="card_id"
    :class="{ card: movie === '', 
              cardImage: movie !== '' }"
    class ="d-flex justify-content-center"
    @click="clickCard"

  > 
    <span class="tooltip-text"><b>{{ movie.title }}</b></span>
  </div>

</template>

<script>
export default {
  name: 'TmdbSearchListItem',
  props: {
    movie: [String, Object],
    item_idx: Number,
  },

  updated () {
    const card = document.querySelector(`#${ this.card_id }`)
    card.style.backgroundImage = this.poster_path ? `url(${ this.poster_path })` : 'none'
  },

  methods: {
    clickCard () {
      // console.log('click', this.movie)
      this.$emit('clickCard', this.movie)
    },
  },

  computed: {
    poster_path () {
      return this.movie.poster_path ? `https://www.themoviedb.org/t/p/w185${ this.movie.poster_path }` : ''
    },

    card_id () {
      return `card${ this.item_idx }`
    }
  },
}
</script>

<style>
.card {
  width: 150px;
  height: 225px;
  margin: 1rem 1rem;

  border-style: none;
  border-radius: 8px;
  background: #ffffff;
  background-image: none;
  box-shadow: inset 7px 7px 18px #dddddd,
              inset -7px -7px 18px #ffffff;
}

.cardImage {
  width: 150px;
  height: 225px;
  margin: 1rem 1rem;

  cursor: pointer;
  border-radius: 8px;
  background: #ffffff;
  background-size: 150px 225px;
  box-shadow: none;
}

.cardImage:hover {
  position: relative;
  box-shadow: inset 8px 8px 20px #000000;
}

/* Tooltip text */
.cardImage .tooltip-text {
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
.cardImage:hover .tooltip-text {
  visibility: visible;
  bottom: 105%;
}
</style>