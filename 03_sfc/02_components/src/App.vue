<template>
    <h3>Übergabe von Attributen in eine Komponente und Verwendung von Default-Werten:</h3>
      <input v-model="msg"/>  {{msg}} => Dieser Wert wird an die Komponente übergeben
      <CCAHeader :msg="msg" />
    <CCAHeader />

    <h3> Events auslösen die sich auf die Hauptkomponente auswirken</h3>
  <BlogEntry/> <!-- Verwenden der Default-Values -->
  <BlogEntry v-for="blog in blogs" :entry="blog" @blogclick="blog_click" />
  <div v-if="curr_id != 0">Aktueller Blog {{curr_id}}</div>
</template>

<style scoped>
</style>


<script>
  import CCAHeader from './components/CCAHeader.vue'
  import BlogEntry from './components/BlogEntry.vue'
  export default {
    components:
        {
          CCAHeader, BlogEntry
        } ,
  data() {
    return {
      msg: 'test',
      blogs : [{id: 1, text: 'entry 1'}, {id: 2, text: 'entry 2'}],
      curr_id : 0

    }
  },
    methods:
        {
          blog_click(id)
          {
            console.log("blog_click");
            this.curr_id = id;
          }
        }
}
</script>

