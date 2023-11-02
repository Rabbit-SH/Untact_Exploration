<template>
<!-- 맵 띄우기 -->
  <MapVue id = 'app'>
  </MapVue>


</template>

<script>
import MapVue from "./components/MapVue.vue"
export default {
  name: 'App',
  components: { MapVue },

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
