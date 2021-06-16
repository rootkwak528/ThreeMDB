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
        <input class="form-control" type="password" id="password" v-model="credentials.password" @keyup.enter="login">
      </div>

      <button class="btn btn-outline-secondary mb-3" @click="login">로그인</button>

      <div v-if="errors" class="fade-in mb-3">
        <span>{{ errors }}</span>
      </div>

      <p class="signup-info">
        아직 회원이 아니신가요? <span class="link" @click="toSignup">회원가입</span>
      </p>

    </div>
    
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
      errors: null,
    }
  },

  created () {
    
    const msg = localStorage.getItem( 'msg' )
    if ( msg ) {

      localStorage.removeItem( 'msg' )
      this.errors = msg

    }

  },

  methods: {
    login () {
      this.errors = null
      
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'TmdbSearch' })
        })
        .catch(err => {
          console.log(err)
          this.errors = 'ID와 비밀번호를 확인해주세요.'
        })
    },

    toSignup () {

      this.$router.push({ name: 'Signup' })

    }
  }
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