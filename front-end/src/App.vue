<template>
  <div id="app">
    <Navi />
    <Map />
  </div>

 </template>
 
 <script>
 import Map from './components/MapView2.vue';
 import Navi from './components/NaviView.vue';
 export default {
  name: 'App',
  components: {
    Map,
    Navi,
  },
 }
 </script>
 
 <style>

 </style>