

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
          // Object/Array defaults must be factory functions, otherwise all instances share one object
          default: () => ({id: 0, text: 'default'})
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