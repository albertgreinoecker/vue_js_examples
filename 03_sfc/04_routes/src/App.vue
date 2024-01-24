<template>
  <p>Bitte die aktuelle Ansicht auswählen:</p>

  <h2>Direkt als Button:</h2>

  <button @click="$router.push('/home')">Home</button>
  <button @click="$router.push('/about')">About</button>
  <button @click="$router.push('/contact')">Contact</button><br>
  <button @click="$router.push('/user/' + user)">Contact</button><br>

  <h2>Als Link:</h2>

  <router-link to="/">Home</router-link> |
  <router-link to="/about">About</router-link> |
  <router-link to="/contact">Contact</router-link><br>
  <router-link :to="'/user/' +user">User</router-link><br>

  <div>
    <router-view></router-view>
  </div>
</template>

<script>
    export default {
      data() {
        return {
          user : "Hubert"
        }
      },
      methods: {
        about: function () {
          console.log("about");
          this.activeComp = 'about';
        }
      }
    }
</script>