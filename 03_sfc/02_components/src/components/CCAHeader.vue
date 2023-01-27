<template>
  <div class="greetings">
      <table>
          <tr>
            <td><img alt="HTL logo" class="logo" src="../assets/htl-anichstrasse-logo.svg" width="125" height="125" /></td>
            <td vertical-align="center">{{ msg }}</td>
      </tr>
      </table>
  </div>
</template>

<style scoped>

</style>


<script>
export default {
  props : {
    msg:
        {
          type : String,
          default: "the default string"
        }
  },
  data() {
    return {
      count: 0
    }
  }
}
</script>