<template>
  <div id="signup-window">

    <div class="signup-form">

      <h1 class="mb-3">Signup</h1>

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

      <div v-if="errors" class="fade-in mb-3">
        <span>{{ errors }}</span>
      </div>

    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'Signup',
  data () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
    }
  },

  computed: {
    ...mapState([
      'isDesktopPlatform',
      'errors',
    ]),
  },

  methods: {
    ...mapActions([
      'signup',
      'setErrors',
    ]),
  },

  created () {
    if (!this.isDesktopPlatform) {
      this.$router.push({ name: 'MobileAlert' })
    }
    
    this.setErrors( null )
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
