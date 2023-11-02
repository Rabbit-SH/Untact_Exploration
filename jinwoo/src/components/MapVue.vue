<template>
  <div id = "map">
    <button @click="getCurrentPosition" style="position: absolute; bottom: 20px; right: 20px; z-index: 1000;">현위치</button>
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
    <l-tile-layer :url="url"></l-tile-layer>
    </l-map>
  </div>
</template>
   
<script>

import L from 'leaflet';
import { LMap, LTileLayer } from 'vue2-leaflet';
import {Icon} from 'leaflet';

import markerImg from 'leaflet/dist/images/marker-icon.png';
import markerShadowImg from 'leaflet/dist/images/marker-shadow.png';
import markerRetinaImg from 'leaflet/dist/images/marker-icon-2x.png';
import 'leaflet/dist/leaflet.css';
import "leaflet-gpx";

export default {
  components: {
    LMap,
    LTileLayer
    // ,iconVue
  },
  mounted(){
    delete Icon.Default.prototype._getIconUrl;
    Icon.Default.mergeOptions({ //marker-icon-2x.png 이미지 파일을 못찾는 에러 제거 코드
      iconRetinaUrl: markerRetinaImg,
      iconUrl: markerImg,
      shadowUrl: markerShadowImg,
    }),
    this.loadGPX();
    this.currentPosIcon = L.icon({
      iconUrl: require('@/assets/logo.png'), // 원하는 마커 이미지로 교체
      iconSize: [32, 32],   // 아이콘 크기 조절
      iconAnchor: [16, 32], // 아이콘 위치 조절
    });
  },



  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      center: [ 37.408473, 128.045787 ],
      zoom: 15,
      bounds: null, //지도 경계가 변경될 때 발생하는 이벤트(드래그되거나 확대/축소 시 발생)
      mapOptions: {
        minZoom: 14, //최소 줌 레벨 설정
        maxZoom: 18
      },
      positionObj: {},
      isPositionReady: false,
      marker: null
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
    openP() {
      this.popVal1 = true;
    },
    closeP(){
      this.popVal1 = false;
    },
    loadGPX() {
      // GPX 파일 로드 및 지도에 표시
      const gpxUrl = process.env.BASE_URL + 'road.gpx'; // 여기에 GPX 파일의 URL을 입력
      new L.GPX(gpxUrl, {
        async: true,
        marker_options: {
          startIconUrl: '',
          endIconUrl: '',
          shadowUrl: '',
          wptIconUrls: {       // 중간 waypoint 마커 이미지
        '': require('@/assets/logo.png'),  // 여기에 사용자 정의 이미지 경로 입력
      },
        }
      }).on("loaded", (e) => {
        this.$refs.map.mapObject.fitBounds(e.target.getBounds());
      }).addTo(this.$refs.map.mapObject);
    },
    getCurrentPosition () {
      if (!navigator.geolocation) {
        this.setAlert('위치 정보를 찾을 수 없습니다.1')
      } else {
        navigator.geolocation.getCurrentPosition(this.getPositionValue, this.geolocationError)
      }
    },
    getPositionValue (val) {
      this.positionObj.latitude = val.coords.latitude
      this.positionObj.longitude = val.coords.longitude
      this.currentPos = [this.positionObj.latitude, this.positionObj.longitude]
      this.isPositionReady = true
      this.marker = L.marker(this.currentPos, { icon: this.currentPosIcon }).addTo(this.$refs.map.mapObject);
      this.$refs.map.mapObject.setView(this.currentPos, 18);
      this.setAlert('주소 확인 완료')
    },
    geolocationError () {
      this.setAlert('위치 정보를 찾을 수 없습니다.2')
    },
    setAlert (text) {
      alert(text)
    }
  },
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
.icon{
  height:50px;
  width: 50px;
}

</style>