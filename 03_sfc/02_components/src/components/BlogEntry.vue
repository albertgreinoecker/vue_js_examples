

<template>
  <div class="greetings">
      <table>
          <tr>
            <td>  <button @click="$emit('blogclick',entry.id)">{{entry.id}}</button></td>
            <td>{{entry.text }}</td>
      </tr>
      </table>
  </div>
</template>

<style scoped>

</style>


<script>
export default {
  props : {
    entry:
        {
          type : Object,
          default: {id: 1, text: 'default'}
        }
  },
  emits: ['blogclick'],

  data() {
    return {
      count: 0
    }
  }
}
</script>