<template>
  <div id="app">

    <!-- loading spinner -->
    <div v-if="loading" id="loading" class="text-light">
      <div class="spinner-border"></div>
      <h1>Loading..</h1>

      <div id="loading-message">
        <p><br>
          <i class="em em-construction" aria-role="presentation" aria-label="BIRD"></i>
          <i class="em em-construction" aria-role="presentation" aria-label="BIRD"></i><br><br>
          저희가 Amazon 무료 플랜을 사용중이예요.<br>
          아마 이 메시지가 보이신다면<br>
          높은 확률로 서버가 켜지고 있는 중일 겁니다.<br>
          조금만 더 기다려주세요.<br>
          서버가 한 번 켜지면 그때부턴 빠를 거예요.<br><br>
          <i class="em em-woman-running" aria-role="presentation" aria-label=""></i>
          <i class="em em-man-running" aria-role="presentation" aria-label=""></i>
          <i class="em em-woman-running" aria-role="presentation" aria-label=""></i>
          <i class="em em-man-running" aria-role="presentation" aria-label=""></i>
        </p>
      </div>
    </div>

    <div id="nav">
      <router-link :to="{ name: 'TmdbSearch' }">TMDB Search</router-link> |
      <span v-if="authToken">
        <router-link @click.native="logout" to="#">Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link> 
      </span>
    </div>
    <router-view @login="isLogin = true"/>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'App',

  computed: {
    ...mapState([
      'loading',
      'authToken',
    ]),
  },

  methods: {
    ...mapActions([
      'logout',
    ]),
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#loading {
  position: absolute;
  height: 100%;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1;
  padding-top: 40%;
}

#loading-message {
  animation-duration: 3s;
  animation-name: fadein;
}

@keyframes fadein {
  0% {
    opacity: 0;
  }

  60% {
    opacity: 0;
  }

  100% {
    opacity: 100;
  }
}
</style>
