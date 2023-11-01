<template>
    <l-marker
      :key="marker.id"
      :lat-lng="marker.coordinates"
    >
      <l-icon ref="icon">
        <img class="marker-ggomi-icon" :src="marker.imageUrl"/>
      </l-icon>
      <l-tooltip>{{ marker.name }}</l-tooltip>
    </l-marker>
   </template>
   
   <script>
   import { LIcon, LMarker, LTooltip } from 'vue2-leaflet'
   export default {
    components: { LIcon, LMarker, LTooltip },
    props: {
      marker: {
        type: Object,
        required: true
      }
    }
   }
   </script>
   
   <style>
    .marker-ggomi-icon {
      height: 50px;
      width: auto;
    }
    </style>
