<template>
  <div id="signup-window">

    <div class="signup-form">

      <h1 class="mb-3">Signup</h1>

      <div v-if="errors" class="fade-in mb-3">
        <span>{{ errors }}</span>
      </div>

      <div class="form-group mb-3">
        <label for="username">사용자 이름: </label>
        <input class="form-control" type="text" id="username" v-model="credentials.username">
      </div>
      
      <div class="form-group mb-3">
        <label for="password">비밀번호: </label>
        <input class="form-control" type="password" id="password" v-model="credentials.password">
      </div>
      
      <div class="form-group mb-4">
        <label for="passwordConfirmation">비밀번호 확인: </label>
        <input class="form-control" type="password" id="passwordConfirmation" 
          v-model="credentials.passwordConfirmation" 
          @keyup.enter="signup(credentials)">
      </div>

      <button class="btn btn-outline-secondary mb-3" @click="signup(credentials)">회원가입</button>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
      errors: null,
    }
  },
  methods: {
    signup () {
      this.errors = null

      if ( !this.credentials.username ) {

        this.errors = 'ID를 입력해주세요.'

      } else if ( !this.credentials.password ) {

        this.errors = '비밀번호를 입력해주세요.'

      } else if ( !this.credentials.passwordConfirmation ) {

        this.errors = '비밀번호 확인을 입력해주세요.'

      } else {
        
        axios({
          method: 'post',
          url: `${SERVER_URL}/accounts/signup/`,
          data: this.credentials,
        })
          .then(res => {
            console.log(res)
            this.$router.push({ name: 'Login' })
          })
          .catch(err => {
            console.log(err)
            if (err.response.data.error) {
              this.errors = err.response.data.error
            } else if (err.response.data.username) {
              this.errors = err.response.data.username[0]
            }
          })

      }
    }
  }
}
</script>

<style>
#signup-window {
  padding-top: 100px;
  background-color: white;
  height: 100vh;
  text-align: left;
}

.signup-form {
  position: absolute;
  top: 20vh;
  left: 40vw;
}

#signup-window label {
  width: 200px;
}

#signup-window input, button {
  width: 20vw;
}
</style>
