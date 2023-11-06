<template>
  <div class="main">    
    <l-map
      style="height: 100%; width: 100%"
      :center="center"
      :zoom="zoom"
      :zoomAnimation=true
      :options="mapOptions"
      class="map"
      ref="map"
      @update:zoom="zoomUpdated"
      @update:center="centerUpdated"
      @update:bounds="boundsUpdated"
    >
      <pop1 :show="popVal1" @close="closeP" class="popup" :class="{'show':popVal1}" />
      <pop2 :show="popVal2" @close="closeP" class="popup" :class="{'show':popVal2}" />
      <pop3 :show="popVal3" @close="closeP" class="popup" :class="{'show':popVal3}" />
      <pop4 :show="popVal4" @close="closeP" class="popup" :class="{'show':popVal4}" />
      <pop5 :show="popVal5" @close="closeP" class="popup" :class="{'show':popVal5}" />

      <LMarker
        :key="markers[0].id"
        :lat-lng="markers[0].coordinates"
        @click="openP"
        :icon="customIcon" />

      <LMarker
        :key="markers[1].id"
        :lat-lng="markers[1].coordinates"
        @click="openP"
        :icon="customIcon" />

      <LMarker
        :key="markers[2].id"
        :lat-lng="markers[2].coordinates"
        @click="openP"
        :icon="customIcon" />

      <LMarker
        :key="markers[3].id"
        :lat-lng="markers[3].coordinates"
        @click="openP"
        :icon="customIcon" />

      <LMarker
        :key="markers[4].id"
        :lat-lng="markers[4].coordinates"
        @click="openP"
        :icon="customIcon" />

      <l-tile-layer :url="url" :attribution="attribution"/>

      <input type="button" value="내 위치" @click="ZoomInToCurrentPosition" :class="{'location-button' : !isZoom, 'location-button-red' : isZoom }" class="my-location-button">
      <input type="button" value="탐방로" @click="goToCenter" class="center-button">

      <l-control-zoom position="bottomleft"></l-control-zoom>

    </l-map>
  </div>
</template>
   
<script>
import { LMap, LTileLayer, LControlZoom, LMarker } from 'vue2-leaflet';
import { L, ICon } from 'leaflet';

import pop1 from '../components/popView1.vue';
import pop2 from '../components/popView2.vue';
import pop3 from '../components/popView3.vue';
import pop4 from '../components/popView4.vue';
import pop5 from '../components/popView5.vue';

import 'leaflet/dist/leaflet.css';
import 'leaflet-gpx';

import markerImg from 'leaflet/dist/images/marker-icon.png';
import markerShadowImg from 'leaflet/dist/images/marker-shadow.png';
import markerRetinaImg from 'leaflet/dist/images/marker-icon-2x.png';

export default {
  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      // center: [ 37.40436362096728, 128.0495492913938], // 처음 지도의 중심이 되는 좌표 / 각 포인트들의 중점
      center: [37.4148911042466, 128.05010676384],
      zoom: 14, // 초기 확대 레벨
      previousZoom : null, //현재의 확대 레벨
      bounds: null, //지도 경계가 변경될 때 발생하는 이벤트(드래그되거나 확대/축소 시 발생)

      popVal1 : false, //pop1이 열려있나 닫혀있나 여부 저장(default=false)
      popVal2 : false,
      popVal3 : false,
      popVal4 : false,
      popVal5 : false,

      isZoomIn: false, //줌인이 된 상태인지 아닌지 확인(팝업창 띄우기 위한 변수)
      isZoom : false, //내 위치 버튼을 위한 줌인 상태 확인 변수
      current : [0,0], // ZoomInToCurrentPosition 메서드에서 버튼 누른 시점의 위치 저장을 위한 변수

      isPositionReady : false,
      positionObj: {
        latitude: 0,
        longitude: 0
      },
      marker: null,

      mapOptions: {
        minZoom: 13, //최소 줌 레벨 설정
        maxZoom: 18,  //최대 줌 레벨 설정
        zoomControl: false, // 줌 컨트롤러 위치를 바꿔줄 예정(왼쪽 상단 -> 왼쪽 하단)
      },
    };
  },
  components: {
    LMap,
    LTileLayer,
    LControlZoom,
    LMarker,
    ICon,
    pop1,
    pop2,
    pop3,
    pop4,
    pop5,
  },
  mounted(){

    delete Icon.Default.prototype._getIconUrl;
    Icon.Default.mergeOptions({ //marker-icon-2x.png 이미지 파일을 못찾는 에러 제거 코드
      iconRetinaUrl: markerRetinaImg,
      iconUrl: markerImg,
      shadowUrl: markerShadowImg,
    });

    // gpx 파일을 위한 코드
    this.loadGPX();

    // 현재 위치 불러오는 코드
    this.getCurrentPosition();
    this.currentPosIcon = L.icon({
      iconUrl: require('@/assets/logo.png'),
      iconSize: [16,16],
      iconAnchor: [16,32]
    });

  },
  methods: {
    zoomUpdated (zoom) {
      this.zoom = zoom;
    },
    centerUpdated (center) {
      this.center = center;
    },
    boundsUpdated(bounds) {
      this.bounds = bounds;
    },
    openP(index){
      setTimeout(()=>{ // 0.7초 뒤 팝업 열림
        this['popVal' + (index+1)] = true;
      }, 700); 
    },
    closeP(){
      this.popVal1 = false;
      this.popVal2 = false;
      this.popVal3 = false;
      this.popVal4 = false;
      this.popVal5 = false;

      if (this.isZoomIn) {
        // 팝업이 닫힌 후 줌 아웃(원래 줌 레벨로 돌아가기)
        this.$refs.map.mapObject.setZoom(this.previousZoom);
        this.isZoomIn = false;
      }
    }, 

    getPositionValue(pos) {
      this.positionObj.latitude = pos.coords.latitude;
      this.positionObj.longitude = pos.coords.longitude;
      this.currentPos = [this.positionObj.latitude, this.positionObj.longitude];
      this.isPositionReady = true;
       
      if (this.$refs.map && this.$refs.map.mapObject) {
        // 이컨 마커가 있다면 삭제 (안하면 위치 변동될때마다 계속 마커가 찍힘)
        if(this.marker){
          this.$refs.map.mapObject.removeLayer(this.marker)
        }
        // 새 마커 추가
        this.marker = L.marker(this.currentPos, {icon: this.currentPosIcon}).addTo(this.$refs.map.mapObject);
      }
    },
    getCurrentPosition(){
      if(!navigator.geolocation){
        alert('위치 정보를 찾을 수 없습니다.')
      } else {
        navigator.geolocation.watchPosition(this.getPositionValue, 
        ()=>alert('위치 정보를 찾을 수 없습니다.2')) //위치 업데이트 시 호출되는 함수 getPositionValue, 오류 발생 시 경고메세지 표시
      }
    },
    FixedCurrentPosition() {
      this.$refs.map.mapObject.setView(this.currentPos, this.zoom);
        this.isZoom = false;
    }, // 토글로 바꿔야겠다

    ZoomInToCurrentPosition(){
      if(this.isZoom) {
        // 버튼을 한번 더 누르면 실시간 현재 내 위치가 지도의 중심으로 고정
        this.$refs.map.mapObject.setView(this.currentPos, this.zoom);
        this.isZoom = false;
      } else {
        this.current = this.currentPos; //currentPos는 실시간으로 변하는 위치를 감지하기 때문에 변하지 않도록 다른 변수에 현재 위치 저장
        this.$refs.map.mapObject.setView(this.current, 16);
        this.isZoom = true;
      } 
    },

    goToCenter(){
      this.$refs.map.mapObject.setView([37.408473, 128.045787],14);
    },
    loadGPX(){
      //.gpx 파일 로드 및 지도에 표시
      const gpxUrl = process.env.BASE_URL + '치악산 탐방서비스 등산로.gpx'
      new L.GPX(gpxUrl, {
        async: true,
        marker_options: {
          startIconUrl: '',
          endIconUrl: '',
          shadowUrl: '',
          wptIconUrls: {       // 중간 waypoint 마커 이미지
            '': require('@/assets/ggomi.png'),  // 여기에 사용자 정의 이미지 경로 입력
          },
        }
      }).on('addpoint', (e) => {
        // waypoint에 이벤트 리스너 추가
        let waypointName = e.point._popup._content;
        waypointName = waypointName.replace(/<[^>]*>?/gm, '');
        e.point.on('click', ()=>{
          switch(waypointName) {
            case '치악산국립공원사무소':
              if(! this.isZoomIn){
                this.previousZoom = this.zoom;
                // 먼저 줌인 액션 실행
                this.$refs.map.mapObject.setZoomAround([e.point._latlng.lat, e.point._latlng.lng], 18);
                this.isZoomIn = true;
              }
              this.openP(0);
              break;
            case '구룡자동차야영장':
            if(! this.isZoomIn){
                this.previousZoom = this.zoom;
                // 먼저 줌인 액션 실행
                this.$refs.map.mapObject.setZoomAround([e.point._latlng.lat, e.point._latlng.lng], 36);
                this.isZoomIn = true;
              }
              this.openP(1);
              break;
            case '황장목숲길':
              if(! this.isZoomIn){
                this.previousZoom = this.zoom;
                // 먼저 줌인 액션 실행
                this.$refs.map.mapObject.setZoomAround([e.point._latlng.lat, e.point._latlng.lng], 36);
                this.isZoomIn = true;
              }
              this.openP(2);
              break;
            case '구룡사':
              if(! this.isZoomIn){
                this.previousZoom = this.zoom;
                // 먼저 줌인 액션 실행
                this.$refs.map.mapObject.setZoomAround([e.point._latlng.lat, e.point._latlng.lng], 36);
                this.isZoomIn = true;
              }
              this.openP(3);
              break;
            case '자생식물관찰원':
              if(! this.isZoomIn){
                this.previousZoom = this.zoom;
                // 먼저 줌인 액션 실행
                this.$refs.map.mapObject.setZoomAround([e.point._latlng.lat, e.point._latlng.lng], 36);
                this.isZoomIn = true;
              }
              this.openP(4);
              break;
          }
        });
      })      
      .on("loaded", (e) => {
        console.log(e.target.getBounds());
        this.$nextTick(() => {
          this.$refs.map.mapObject.setView(this.center, this.zoom);
        });
      }).addTo(this.$refs.map.mapObject);
    },
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
  .icon{
    height:50px;
    width: 50px;
  }
  .popup{
    /* 트랜지션 속성을 추가하여 부드러운 나타남 및 사라짐 만들기 */
    transition: opacity 0.5s; 
    opacity: 0; /*초기에 투명상태로 설정*/
  }
  .popup.show{
    opacity: 1; /*나타날 때 투명도를 1로 설정하여 부드럽게 나타나게 함*/
  } 
  .my-location-button {
    z-index: 1001;
    position: absolute;
    bottom: 150px;
  }
  .center-button {
    z-index: 1001;
    position: absolute;
    bottom: 100px;
  }
  .location-button-red {
    background-color: red;
    color: white;
  }
</style>