<template>
  <div>
    <input v-model="name"/> <br/><br/><br/>
  </div>
  <br/>
  <span class="hello"> Hallo {{ name }} </span><br/>
  <button @click="count++">Anzahl der Clicks: {{ count }}</button>
</template>

<style>
button {
  font-weight: bold;
  background: aquamarine;
}
.hello
{
  font-size: large;
}
</style>
<script>
export default {
  data() {
    return {
      count: 0,
      name: "Hubert"
    }
  }
}
</script>

