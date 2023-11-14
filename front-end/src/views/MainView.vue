<template>
    <div id="app">
      <Navi />
      <Map  />
    </div>
  
   </template>
   
   <script>
   import Map from '../components/MapView.vue';
   import Navi from '../components/NaviView.vue';
   export default {
    name: 'MainView',
    components: {
      Map,
      Navi,
    },
    data(){
      return{

      }
    },
    methods:{

    }

   }
   </script>
   
   <style>
  
   </style>