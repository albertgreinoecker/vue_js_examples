<template>
    <h1>User</h1>
    Das ist die Homebase von: {{name}}
  </template>
  
  <script>
    export default {
      data() {
        return {
        }
      },
      computed: {
        name() {
          return this.$route.params.name + " der nette";
        }
      }
    }
  </script>