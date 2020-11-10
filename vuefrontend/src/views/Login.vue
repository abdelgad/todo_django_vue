<template>
  <div class="login-form">
  <form v-on:submit.prevent="login">
    <h1>Login</h1>
    <div class="content">
      <div class="input-field">
        <input type="text" name="username" v-model="username" placeholder="Username">
      </div>
      <div class="input-field">
        <input type="password" name="password" v-model="password" placeholder="Password" autocomplete="new-password">
      </div>
      <p v-if="incorrectAuth" class="error-message">Incorrect username or password entered !</p>
    </div>
    <div class="action">
      <button type="submit">Register</button>
      <button type="submit">Sign in</button>
    </div>
  </form>
</div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: '',
      incorrectAuth: false
    }
  },
  methods: {
    login () {
      this.$store.dispatch('userLogin', {
        username: this.username,
        password: this.password
      })
      .then(() => {
        this.$router.push({ name: 'home'})
      })
      .catch(err => {
        console.log(err)
        this.incorrectAuth = true
      })
    }
  }
}
</script>

<style lang="scss">
// Basic reset
* {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
  font-family: sans-serif;
}

.login-form {
  background: #fff;
  width: 500px;
  margin: 65px auto;
  display: flex;
  flex-direction: column;
  border-radius: 4px;
  box-shadow: 0 2px 25px rgba(0, 0, 0, 0.2);

  h1 {
    padding: 35px 35px 0 35px;
    font-weight: 300;
  }

  .content {
    padding: 35px;
    text-align: center;
  }

  .input-field {
    padding: 12px 5px;
    input {
      font-size: 16px;
      display: block;
      font-family: sans-serif;
      width: 100%;
      padding: 10px 1px;
      border: 0;
      border-bottom: 1px solid #747474;
      outline: none;
      transition: all .2s;
      &::placeholder {
        text-transform: uppercase;
      }

      &:focus {
        border-color: #222;
      }
    }
  }

  a.link {
    text-decoration: none;
    color: #747474;
    letter-spacing: 0.2px;
    text-transform: uppercase;
    display: inline-block;
    margin-top: 20px;
  }

  .action {
    display: flex;
    flex-direction: row;
    button {
      width: 100%;
      border: none;
      padding: 18px;
      font-family: sans-serif;
      cursor: pointer;
      text-transform: uppercase;
      background: #e8e9ec;
      color: #777;
      border-bottom-left-radius: 4px;
      border-bottom-right-radius: 0;
      letter-spacing: 0.2px;
      outline: 0;
      transition: all .3s;

      &:hover {
        background: #d8d8d8;
      }

      &:nth-child(2) {
        background: #008B8B;
        color: #fff;
        border-bottom-left-radius: 0;
        border-bottom-right-radius: 4px;

        &:hover {
          background: #117979;
        }
      }
    }
  }

  p.error-message {
    color: #A64452;
    margin-top: 10px;
  }

}
</style>
