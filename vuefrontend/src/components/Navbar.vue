<template>
  <div id="navigation-bar">
    <nav>
      <ul>
        <li><a href="#" id="logo">TODO</a></li>
        <li><router-link :to = "{ name: 'home' }">Home</router-link></li>
        <li v-if="accessToken!=null"><router-link :to = "{ name:'logout' }">Logout</router-link></li>
      </ul>
    </nav>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'NavBar',
  computed: mapState(['accessToken'])
}
</script>

<style lang="scss">
nav {
  overflow: hidden;
  background-color: #008B8B;
  top: 0;
  width: 100%;
  ul {
    text-align: center;
    list-style-type: none;
    list-style-type: none;
    margin: 0;
    padding: 15px;
    li {
      display: inline;
      font-family: sans-serif;
      font-size: 17px;
      a {
        color: #f2f2f2;
        text-decoration: none;
        padding: 14px;
        &:hover {
          background-color: #A9A9A9;
        }
      }
    }
  }
}
</style>
