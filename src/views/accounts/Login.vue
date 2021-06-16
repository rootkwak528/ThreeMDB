<template>
  <div id="login-window">

    <div class="login-form">

      <h1 class="mb-3">Login</h1>

      <div class="form-group mb-3">
        <label for="username">사용자 이름: </label>
        <input class="form-control" type="text" id="username" v-model="credentials.username">
      </div>

      <div class="form-group mb-4">
        <label for="password">비밀번호: </label>
        <input class="form-control" type="password" id="password" v-model="credentials.password" @keyup.enter="login(credentials)">
      </div>

      <button class="btn btn-outline-secondary mb-3" @click="login(credentials)">로그인</button>

      <p class="signup-info mb-3">
        아직 회원이 아니신가요? <span class="link" @click="toSignup">회원가입</span>
      </p>

      <div v-if="errors" class="fade-in mb-3">
        <span>{{ errors }}</span>
      </div>

    </div>
    
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Login',
  data () {
    return {
      credentials: {
        username: null,
        password: null,
      },
    }
  },

  computed: {
    ...mapState([
      'errors',
    ]),
  },

  methods: {
    ...mapActions([
      'login',
      'setErrors',
    ]),

    toSignup () {
      this.$router.push({ name: 'Signup' })
    }
  },

  created () {
    if ( this.errors !== '먼저 로그인을 해야 합니다.' ) {
      this.setErrors( null )
    }
  },
}
</script>

<style>
#login-window {
  padding-top: 100px;
  background-color: white;
  height: 100vh;
  text-align: left;
}

.login-form {
  position: absolute;
  top: 20vh;
  left: 40vw;
}

#login-window label {
  width: 20vw;
}

#login-window input, button {
  width: 20vw;
}

.signup-info {
  font-size: 0.8rem;
}

.link {
  color: #41B883;
}

.link:hover {
  cursor: pointer;
}

.fade-in {
  animation: fadeIn ease 1s;
  color: crimson;
  font-size: 0.8rem;
}

@keyframes fadeIn{
  0% {
    opacity:0;
  }
  100% {
    opacity:1;
  }
}
</style>