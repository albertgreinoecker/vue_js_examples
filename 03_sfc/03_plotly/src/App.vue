<template>
    <VuePlotly :data="data" :layout="layout"></VuePlotly>
</template>

<script>

 import { VuePlotly } from 'vue3-plotly';

export default {
  components: {
    VuePlotly
  },
  data() {
    return {
      data:[{"x": ["Gold", "Silver", "Bronze"], "y": [31, 84, 51], "type": "bar"}],
      layout:{
        title: "My graph"
      }
    }
  }
}
</script>