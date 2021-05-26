<template>
  <div 
    :id="card_id"
    :class="{ card: movie === '', 
              cardImage: movie !== '' }"
    @click="clickCard"
  > </div>
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
  box-shadow: inset 8px 8px 20px #000000;
}
</style>