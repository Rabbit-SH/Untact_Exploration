<template>
  <l-map
    style="height: 100%;, width: 100%"
    :center="center"
    :zoom="zoom"
    :options="mapOptions"
    class="map"
    ref="map"
    @update:zoom="zoomUpdated"
    @update:center="centerUpdated"
    @update:bounds="boundsUpdated"
  >
    <iconVue
      v-for="marker in markers"
      :marker="marker"
      :key="marker.id"
      :lat-lng="marker.coordinates">
    </iconVue>
    <l-tile-layer
      :url="url"
    >
    </l-tile-layer>
  </l-map>
</template>
   
<script>
import { LMap, LTileLayer } from 'vue2-leaflet';
import {Icon} from 'leaflet';
import iconVue from '../components/iconVue.vue'
import markerImg from 'leaflet/dist/images/marker-icon.png';
import markerShadowImg from 'leaflet/dist/images/marker-shadow.png';
import markerRetinaImg from 'leaflet/dist/images/marker-icon-2x.png';
import 'leaflet/dist/leaflet.css';
export default {
  components: {
    LMap,
    LTileLayer,
    iconVue,
  },
  mounted(){
    delete Icon.Default.prototype._getIconUrl;
    Icon.Default.mergeOptions({ //marker-icon-2x.png 이미지 파일을 못찾는 에러 제거 코드
      iconRetinaUrl: markerRetinaImg,
      iconUrl: markerImg,
      shadowUrl: markerShadowImg,
    });
  },
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      // customImageUrl: require('@/assets/dudu.png'),
      center: [ 37.408473, 128.045787 ],
      zoom: 14,
      bounds: null, //지도 경계가 변경될 때 발생하는 이벤트(드래그되거나 확대/축소 시 발생)
      mapOptions: {
        minZoom: 14, //최소 줌 레벨 설정
        maxZoom: 18
      },
      markers:[ // 아이콘 포인트 표시 지정
        {id:1, coordinates:[37.414726, 128.050078], name: '체험학습관',
          imageUrl: require('@/assets/ggomi.png')}, // 체험학습관
        {id:2, coordinates:[37.408449, 128.045788], name: '구룡야영장',
          imageUrl: require('@/assets/ggomi.png')}, // 구룡야영장
        {id:3, coordinates:[37.40535807810431, 128.048564036553], name: '황장숲목길',
          imageUrl: require('@/assets/ggomi.png')}, // 황장숲목길
        {id:4, coordinates:[37.399378, 128.049886], name: '구룡사',
          imageUrl: require('@/assets/ggomi.png')}, // 구룡사
        {id:5, coordinates:[37.395018, 128.053136], name: '자생식물관찰원',
          imageUrl: require('@/assets/ggomi.png')}, // 자생식물관찰원
      ],
    }
  },
  methods: {
    zoomUpdated (zoom) {
      this.zoom = zoom;
      // console.log(this.markers)
    },
    centerUpdated (center) {
      this.center = center;
    },
    boundsUpdated(bounds) {
      this.bounds = bounds;
    },
    // showTooltip(marker){
    //   marker.showTooltip = true;
    // },
    // hideTooltip(marker){
    //   marker.showTooltip = false;
    // }
  }
}
</script>

<style>
.map {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow :hidden
}
.marker-ggomi-icon {
  height: 50px;
  width: auto;
}
</style>