<template>
  <div :id="card_id"
    :class="{ card: movie === '', 
              cardImage: movie !== '' }">
    
  </div>
</template>

<script>
export default {
  name: 'TmdbSearchListItem',
  props: {
    movie: [String, Object],
    item_id: Number,
  },
  methods: {
    onClickItem () {
      this.$emit('on-click-item', this.movie)
    },
    change_background_image () {
      const card = document.querySelector(`#${ this.card_id }`)
      card.style.backgroundImage = `url(${ this.poster_path })`
    }
  },
  computed: {
    poster_path () {
      if (this.movie.poster_path) {
        return `https://www.themoviedb.org/t/p/w185${ this.movie.poster_path }`
      } else {
        return ''
      }
    },
    card_id () {
      return `card${ this.item_id }`
    }
  },
  watch: {
    poster_path (val) {
      if (val) {
        setTimeout( this.change_background_image, 0 )
      } else {
        const card = document.querySelector(`#${ this.card_id }`)
        card.style.backgroundImage = 'none'
      }
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
  box-shadow: 0px 0px 0px #ffffff,
               0px 0px 0px #ffffff;
  /* box-shadow:  7px 7px 14px #a7a7a7,
              -7px -7px 14px #ffffff; */
}

.cardImage:hover {
  box-shadow: inset 8px 8px 20px #000000;
}
</style>