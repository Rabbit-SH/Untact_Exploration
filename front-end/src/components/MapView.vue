<template>
  <div class="main">    
    <l-map
      style="height: 100%; width: 100%"
      :center="center"
      :zoom="zoom"
      :zoomAnimation=true
      :options="mapOptions"
      :maxBounds="maxBounds"
      class="map" 
      ref="map"
      @update:zoom="zoomUpdated"
      @update:center="centerUpdated"
      @update:bounds="boundsUpdated"
    >

    <div class="logo">
      <img :src="require('@/assets/logo.png')">
    </div>

    <div class="mission">
      <img :src="require('@/assets/mission.png')" @click="getDurumari">
      <div class="mission-current">
        {{ completedMissionsCount }}/{{ totalMissions }}
      </div>
      
    </div>
    <v-btn
      elevation="2"
      icon
      :color="isZoom ? 'red' : 'blue'"
      class="my-location-button"
      @click="ZoomInToCurrentPosition"
      height = "33px"
      width = "33px"
      style="border-radius: 50%; background-color: white;"
    >
      <v-icon size = "28">mdi-crosshairs-gps</v-icon>
    </v-btn>

      <m1 :show="popVal1" @close="closeP(1)" @answerCorrect="updateResult(1)" class="popup" :class="{'show':popVal1}" />
      <m2 :show="popVal2" @close="closeP(2)" @answerCorrect="updateResult(2)" class="popup" :class="{'show':popVal2}" />
      <m3 :show="popVal3" @close="closeP(3)" @answerCorrect="updateResult(3)" class="popup" :class="{'show':popVal3}" />
      <m4 :show="popVal4" @close="closeP(4)" @answerCorrect="updateResult(4)" class="popup" :class="{'show':popVal4}" />
      <m5 :show="popVal5" @close="closeP(5)" @answerCorrect="updateResult(5)" class="popup" :class="{'show':popVal5}" />
      <m6 :show="popVal6" @close="closeP(6)" @answerCorrect="updateResult(6)" class="popup" :class="{'show':popVal6}" />
      <m7 :show="popVal7" @close="closeP(7)" @answerCorrect="updateResult(7)" class="popup" :class="{'show':popVal7}" />
      <m8 :show="popVal8" @close="closeP(8)" @answerCorrect="updateResult(8)" class="popup" :class="{'show':popVal8}" />
      <m9 :show="popVal9" @close="closeP(9)" @answerCorrect="updateResult(9)" class="popup" :class="{'show':popVal9}" />
      <m10 :show="popVal10" @close="closeP(10)" @answerCorrect="updateResult(10)" class="popup" :class="{'show':popVal10}" />

      <InfoChiakView :show="showInfoChiak" class="infoChiak" :class="{'show': showInfoChiak}" @closeTutorial="closed"/>
      <GiftView :show="allRes" :class="{'show': allRes}" @closeGift="closeLast"/>

      <LMarker
        :key="markers[0].id"
        :lat-lng="markers[0].coordinates"
        @click="openP(0)"
        :icon="result1 ? customIcon: defaultIcon" />

      <LMarker
        :key="markers[1].id"
        :lat-lng="markers[1].coordinates"
        @click="openP(1)"
        :icon="result2 ? customIcon: defaultIcon" 
        v-if="result1 === true" />

      <LMarker
        :key="markers[2].id"
        :lat-lng="markers[2].coordinates"
        @click="openP(2)"
        :icon="result3 ? customIcon: defaultIcon" 
        v-if="result2 === true" />

      <LMarker
        :key="markers[3].id"
        :lat-lng="markers[3].coordinates"
        @click="openP(3)"
        :icon="result4 ? customIcon: defaultIcon"
        v-if="result3 === true" />

      <LMarker
        :key="markers[4].id"
        :lat-lng="markers[4].coordinates"
        @click="openP(4)"
        :icon="result5 ? customIcon: defaultIcon" 
        v-if="result4 === true" />
      
      <LMarker
        :key="markers[5].id"
        :lat-lng="markers[5].coordinates"
        @click="openP(5)"
        :icon="result6 ? customIcon: defaultIcon" 
        v-if="result5 === true" />

      <LMarker
        :key="markers[6].id"
        :lat-lng="markers[6].coordinates"
        @click="openP(6)"
        :icon="result7 ? customIcon: defaultIcon" 
        v-if="result6 === true" />

      <LMarker
        :key="markers[7].id"
        :lat-lng="markers[7].coordinates"
        @click="openP(7)"
        :icon="result8 ? customIcon: defaultIcon" 
        v-if="result7 === true" />

      <LMarker
        :key="markers[8].id"
        :lat-lng="markers[8].coordinates"
        @click="openP(8)"
        :icon="result9 ? customIcon: defaultIcon" 
        v-if="result8 === true" />

      <LMarker
        :key="markers[9].id"
        :lat-lng="markers[9].coordinates"
        @click="openP(9)"
        :icon="result10 ? customIcon: defaultIcon" 
        v-if="result9 === true" />

      <l-circle :lat-lng="currentPos" :radius=circle.radius :color=circle.color />

      <div class="navi-bar">
        <v-btn
          elevation="2"
          icon
          color="teal"
          @click="showTutorialPopup" 
          class="story"
          height = "50px"
          width = "50px"
          style="border-radius: 50%; background-color: white;">
          <v-icon size = "28">mdi-book-open-page-variant-outline</v-icon>
        </v-btn>
        <v-btn
          elevation="2"
          icon
          color="teal"
          @click="getGallery" 
          class="gallery"
          height = "50px"
          width = "50px"
          style="border-radius: 50%; background-color: white;">
          <v-icon size = "28">mdi-image-multiple</v-icon>
        </v-btn>
        <v-btn
          elevation="2"
          icon
          color="teal"
          @click="InfoChiak" 
          class="credit"
          height = "50px"
          width = "50px"
          style="border-radius: 50%; background-color: white;">
          <v-icon size = "28">mdi-text-box-check-outline</v-icon>
        </v-btn>
        <v-btn
          elevation="2"
          icon
          color="teal"
          @click="$router.push({name: 'AIView'})" 
          class="uploadImg"
          height = "80px"
          width = "80px"
          style="border-radius: 50%; background-color: white;">

          <v-icon size = "50">mdi-panorama-variant-outline</v-icon>
        </v-btn>
      </div>
        
      <l-tile-layer :url="url" />

        <TutorialView :show="showtutorial" 
            @closeTutorial="closeTutorial"
            @openTutorial="showTutorialPopup" />
        <Durumari :show="isCredit" @close="closeDurumari"/>
        <GalleryView :show="gallery_open" @close="closeGallery" />
        <UploadImageView :show="uploadIMG" :class="{'show':uploadIMG}" @close="closeUImg"/>

      <div  class="animated-marker" v-show="isGift">
        <img :src="require('@/assets/present.png')" 
        @click="$router.push({name: 'FinalView'})">
      </div>

    </l-map>
  </div>
</template>
   
<script>
import { LMap, LTileLayer, LMarker, LCircle } from 'vue2-leaflet';
import L from 'leaflet';
import { Icon } from 'leaflet';

import EventBus from '@/EventBus.js';

import m1 from '../components/mission/m1View.vue';
import m2 from '../components/mission/m2View.vue';
import m3 from '../components/mission/m3View.vue';
import m4 from '../components/mission/m4View.vue';
import m5 from '../components/mission/m5View.vue';
import m6 from '../components/mission/m6View.vue';
import m7 from '../components/mission/m7View.vue';
import m8 from '../components/mission/m8View.vue';
import m9 from '../components/mission/m9View.vue';
import m10 from '../components/mission/m10View.vue';

import GiftView from '../components/GiftView.vue';

import 'leaflet/dist/leaflet.css';
import 'leaflet-gpx';

import markerImg from 'leaflet/dist/images/marker-icon.png';
import markerShadowImg from 'leaflet/dist/images/marker-shadow.png';
import markerRetinaImg from 'leaflet/dist/images/marker-icon-2x.png';

import Durumari from './NaviView/DurumariView.vue';
import GalleryView from './NaviView/GalleryView.vue';
import TutorialView from './NaviView/TutorialView.vue';
import UploadImageView from './NaviView/UploadImageView2.vue';
import InfoChiakView from './NaviView/InfoChiakView.vue';


// 결과를 세션 스토리지에 저장하는 함수
function saveResultsToLocalStorage(results) {
  sessionStorage.setItem('missionResults', JSON.stringify(results));
}

// 세션 스토리지에서 결과를 가져오는 함수
function getResultsFromSessionStorage() {
  const resultsJSON = sessionStorage.getItem('missionResults');
  return resultsJSON ? JSON.parse(resultsJSON) : {};
}

export default {

  data () {
    return {
      url: 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> '
                    + '&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
      center: [37.4148974953341, 128.050171136856],
      zoom: 16, // 초기 확대 레벨
      previousZoom : null, //현재의 확대 레벨
      bounds: null, //지도 경계가 변경될 때 발생하는 이벤트(드래그되거나 확대/축소 시 발생)
      maxBounds:[
        [37.3721675168233, 128.0170751794774], //남서쪽 경계
        [37.46310508072958, 128.0814481958348] //북동쪽 경계
      ],

      popVal1 : false, //pop1이 열려있나 닫혀있나 여부 저장(default=false)
      popVal2 : false,
      popVal3 : false,
      popVal4 : false,
      popVal5 : false,
      popVal6 : false,
      popVal7 : false,
      popVal8 : false,
      popVal9 : false,
      popVal10 : false,

      result1: false,
      result2: false,
      result3: false,
      result4: false,
      result5: false,
      result6: false,
      result7: false,
      result8: false,
      result9: false,
      result10: false,

      isZoomIn: false, //줌인이 된 상태인지 아닌지 확인(팝업창 띄우기 위한 변수)
      isZoom : false, //내 위치 버튼을 위한 줌인 상태 확인 변수
      isGift: false, //마지막 모든 미션 수행 후 선물 버튼(한국화 변환 + 세그멘테이션)을 나타낼 변수
      current : [0,0], // ZoomInToCurrentPosition 메서드에서 버튼 누른 시점의 위치 저장을 위한 변수
      currentPos: [0,0], // 실시간 내 위치 변화 저장 변수
      showInfoChiak: false,

      isCredit: false,
      gallery_open: false,
      showtutorial: false,
      uploadIMG: false,

      isPositionReady : false,
      positionObj: {
        latitude: 0,
        longitude: 0
      },

      mapOptions: {
        minZoom: 13, //최소 줌 레벨 설정
        maxZoom: 18,  //최대 줌 레벨 설정
        zoomControl: false, // 줌 컨트롤러 위치를 바꿔줄 예정(왼쪽 상단 -> 왼쪽 하단)
      },

      markers: [
        {id:1, coordinates: [37.4148974953341, 128.050171136856], name:'치악산 체험학습관 맛보기 미션'},
        {id:2, coordinates: [37.4047839823339, 128.047338724136], name:'황장금표'},
        {id:3, coordinates: [37.40485112, 128.04897584], name:'황장목숲길 안내판'},
        {id:4, coordinates: [37.403465098361, 128.048915863037], name:'데크길1: 가족사진'},
        {id:5, coordinates: [37.40172059, 128.05039145], name:'데크길 2 : 꺾인 후 지점'},
        {id:6, coordinates: [37.3992934, 128.0498706], name:'구룡사'},
        {id:7, coordinates: [37.39793653, 128.05143569], name:'돌탑 미션'},
        {id:8, coordinates: [37.3972176621091, 128.051402270794], name:'범람로 시작 전 표지판'},
        {id:9, coordinates: [37.3946674, 128.0533533], name:'탄소중립 미션'},
        {id:10, coordinates: [37.3950754, 128.0534256], name:'솔비로길(야생화원)'},
      ],
      defaultIcon: new Icon({  // 지도의 마커 사용자 지정 아이콘(기본 디폴트 아이콘)
        iconUrl: require('@/assets/marker.png'),
        iconSize: [50, 50],
        iconAnchor: [16,32]
      }),
      customIcon: new Icon({  // 정답 시 바뀔 아이콘
        iconUrl: require('@/assets/꺼비위치아이콘.png'),
        iconSize: [60, 60],
        iconAnchor: [16,32]
      }),
      circle: { radius: 5, color: 'blue'}
    };
  },
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LCircle,
    m1,
    m2,
    m3,
    m4,
    m5,
    m6,
    m7,
    m8,
    m9,
    m10,
    InfoChiakView,
    GiftView,
    Durumari,
    GalleryView,
    TutorialView,
    UploadImageView,
  },
  mounted(){
    delete Icon.Default.prototype._getIconUrl;
    Icon.Default.mergeOptions({ //marker-icon-2x.png 이미지 파일을 못찾는 에러 제거 코드
      iconRetinaUrl: markerRetinaImg,
      iconUrl: markerImg,
      shadowUrl: markerShadowImg,
    });

    this.$refs.map.mapObject.attributionControl.setPrefix(''); // attribution을 제거하는 코드

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
    getDurumari(){
      this.isCredit = true;
      this.gallery_open = false;
      this.showtutorial = false;
      this.uploadIMG = false;
    },
    closeDurumari(){
      this.isCredit = false;
      this.gallery_open = false;
      this.showtutorial = false;
      this.uploadIMG = false;
    },
    getGallery(){
            this.gallery_open = true;
            this.showtutorial = false;
            this.uploadIMG = false;
            this.isCredit = false;
            if (this.$refs.map && this.$refs.map.mapObject) {
                this.$refs.map.mapObject.dragging.disable(); //사용자가 마우스나 터치로 지도를 드래그하는 것을 방지
                this.$refs.map.mapObject.scrollWheelZoom.disable(); //사용자가 마우스 휠로 지도를 확대/축소하는 것을 방지
              }
        },
        closeGallery(){
            this.gallery_open = false;
            this.isCredit = false;
            this.showtutorial = false;
            this.uploadIMG = false;
            if (this.$refs.map && this.$refs.map.mapObject) {
              this.$refs.map.mapObject.dragging.enable();
              this.$refs.map.mapObject.scrollWheelZoom.enable();
            }
        },
    closeTutorial(){
      this.isCredit = false;
      this.gallery_open = false;
      this.showtutorial = false;
      this.uploadIMG = false;
    },
    showTutorialPopup(){
      this.showtutorial = true;
      this.uploadIMG = false;
      this.isCredit = false;
      this.gallery_open = false;

    },
    shwoUImg(){
      this.uploadIMG = true;
      this.showtutorial = false;
      this.isCredit = false;
      this.gallery_open = false;
    },
    closeUImg(){
      this.isCredit = false;
      this.gallery_open = false;
      this.showtutorial = false;
      this.uploadIMG = false;
    },
    closeModal(){
      this.showModal = false;
    },

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
      if(! this.isZoomIn){
        this.previousZoom = this.zoom;
        // 먼저 줌인 액션 실행
        const marker = this.markers[index];
        this.$refs.map.mapObject.setZoomAround(marker.coordinates, 36);
        this.isZoomIn = true;
      }
      // 0.8초 뒤 팝업 열기
      setTimeout(()=>{this['popVal' + (index+1)] = true;}, 800);

      // 지도의 드래그와 스크롤 줌 비활성화
      if (this.$refs.map && this.$refs.map.mapObject) {
      this.$refs.map.mapObject.dragging.disable(); //사용자가 마우스나 터치로 지도를 드래그하는 것을 방지
      this.$refs.map.mapObject.scrollWheelZoom.disable(); //사용자가 마우스 휠로 지도를 확대/축소하는 것을 방지
    }

    },
    closeP(idx){
      this.popVal1 = false;
      this.popVal2 = false;
      this.popVal3 = false;
      this.popVal4 = false;
      this.popVal5 = false;
      this.popVal6 = false;
      this.popVal7 = false;
      this.popVal8 = false;
      this.popVal9 = false;
      this.popVal10 = false;
      
      // 지도의 드래그와 스크롤 줌 활성화
      if (this.$refs.map && this.$refs.map.mapObject) {
      this.$refs.map.mapObject.dragging.enable();
      this.$refs.map.mapObject.scrollWheelZoom.enable();
    }

    setTimeout(() => {
      if (this.isZoomIn && idx < 10) {
        // 팝업이 닫힌 후 줌 아웃(원래 줌 레벨로 돌아가기)
        this.$refs.map.mapObject.panTo(this.markers[idx].coordinates, { duration: 0.3 });
        this.$refs.map.mapObject.setView(this.markers[idx].coordinates, this.previousZoom);
        this.isZoomIn = false;
      }
    }, 300);
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

    ZoomInToCurrentPosition(){
      this.current = this.currentPos;
      if (this.isZoom) {
        this.$refs.map.mapObject.setView(this.current, this.Zoom);
        this.isZoom = false;
      } else {
        this.$refs.map.mapObject.setView(this.currentPos, 16);
        this.isZoom = true;
      }
    },

    goToCenter(){
      this.$refs.map.mapObject.setView([37.408473, 128.045787],14);
    },
    loadGPX(){
      //.gpx 파일 로드 및 지도에 표시
      const gpxUrl = process.env.BASE_URL + '1108 치악산 GPS탐방로.gpx'
      fetch(gpxUrl)
      .then(response => response.text())
      .then(data => {
        // GPX 트랙 파싱
        const gpx = new DOMParser().parseFromString(data, 'text/xml');
        const trackCoords = [];
        
        // 트랙 세그먼트 추출
        const trkseg = gpx.getElementsByTagName('trkpt');
        for (let i = 0; i < trkseg.length; i++) {
          const lat = parseFloat(trkseg[i].getAttribute('lat'));
          const lon = parseFloat(trkseg[i].getAttribute('lon'));
          trackCoords.push([lat, lon]);
        }
        
        // 새로운 폴리선(선) 생성
        const polyline = L.polyline(trackCoords, { color: '#C4DEFF', weight: 15, opacity: 0.8 });

        // 맵에 폴리선 추가
        polyline.addTo(this.$refs.map.mapObject);

        // 지도 중심과 확대 설정 (트랙에 맞게 조절)
        // this.$refs.map.mapObject.fitBounds(polyline.getBounds());
        this.$refs.map.mapObject.setView(this.center, this.zoom);
      })
      .catch(error => {
        console.error('Error loading GPX:', error);
      });
    },

    updateResult(id){
      this['result' + (id)]= true;
      const results = {
        result1: this.result1,
        result2: this.result2,
        result3: this.result3,
        result4: this.result4,
        result5: this.result5,
        result6: this.result6,
        result7: this.result7,
        result8: this.result8,
        result9: this.result9,
        result10: this.result10,
      };
      EventBus.$emit('send-results-to-durumari', results);
      saveResultsToLocalStorage(results);
    },
    InfoChiak(){
      this.showInfoChiak = true;
    },
    
    closed(){
      this.showInfoChiak = false;
      this.uploadIMG = false;
    },
    closeLast(){
      this.result1 = false;
      this.result2 = false;
      this.result3 = false;
      this.result4 = false;
      this.result5 = false;
      this.result6 = false;
      this.result7 = false;
      this.result8 = false;
      this.result9 = false;
      this.result10 = false;

      this.isGift = true;
    },
    Good(){
      this.result1 = true;
      this.result2 = true;
      this.result3 = true;
      this.result4 = true;
      this.result5 = true;
      this.result6 = true;
      this.result7 = true;
      this.result8 = true;
      this.result9 = true;
      this.result10 = true;
    }
  },
  computed:{
    allRes(){
      return [this.result1, this.result2, this.result3, this.result4, this.result5, this.result6, this.result7, this.result8, this.result9, this.result10].every(Boolean); 
    },
    completedMissionsCount() {
      return [this.result1, this.result2, this.result3, this.result4, this.result5, this.result6, this.result7, this.result8, this.result9, this.result10].filter(Boolean).length;
    },
    totalMissions() {
      return 10; // 전체 미션의 수
    }
  },
  created(){
    const storedResults = getResultsFromSessionStorage();
    for (const key in storedResults) {
      if (Object.hasOwnProperty.call(storedResults, key)) {
        this[key] = storedResults[key];
      }
    }
  }
}
</script>

<style scoped>
  .map {
    position: absolute;
    width: 100%;
    height: 100%;
    overflow :hidden
  }
  .popup{
    /* 트랜지션 속성을 추가하여 부드러운 나타남 및 사라짐 만들기 */
    transition: opacity 0.5s; 
    opacity: 0; /*초기에 투명상태로 설정*/
  }
  .popup.show{
    opacity: 1; /*나타날 때 투명도를 1로 설정하여 부드럽게 나타나게 함*/
  } 

  .chiakInfo{
    right: 1.5%;
    bottom: 40px;
    z-index: 500;
    position: absolute;
  }
  .chiakInfo img{
    height: 70px;
    width: auto;
  }
  .showUImg{
    right: 2%;
    bottom: 150px;
    z-index: 1001;
    position: absolute;
  }
  .showUImg img{
    height: auto;
    width: 70px;
  }
  
  @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
      transform: translateY(0);
    }
    40% {
      transform: translateY(-30px);
    }
    60% {
      transform: translateY(-15px);
    }
  }


  .animated-marker {
    animation: bounce 1s infinite;
    z-index: 1001;
    position: absolute;
    bottom: 35%; 
    right: 25%;
    /* transform: translate(-50%, -50%); */
  }
  .navi-bar {
  position: fixed; /* 고정 위치 */
  bottom: 3%; /* 화면 하단 */
  left: 50%; /* 화면 중앙 정렬을 위해 왼쪽에서 50% 위치 */
  transform: translateX(-50%); /* 중앙 정렬을 위해 X축으로 -50% 이동 */
  display: flex; /* 내부 요소를 가로로 정렬 */
  justify-content: center; /* 내부 요소들을 중앙에 배치 */
  align-items: center; /* 세로 방향으로 중앙 정렬 */
  z-index: 1001; /* 다른 요소들 위에 표시 */
}

  .navi-bar .story{
    display: absolute;
    align-items: center;
    z-index: 1001;
    margin-left: 30px;
    margin-right: 30px;
  }
  .navi-bar .gallery{
    display: absolute; 
    align-items: center;
    z-index: 1001;
    margin-right: 30px;
  }
  .navi-bar .credit{
    display: absolute; 
    align-items: center;
    z-index: 1001;
    margin-right: 30px;
  }
  .navi-bar .uploadImg{
    display: absolute;
    align-items: center;
    z-index: 1001;
    margin-right: 30px;
  }
  .logo {
    position: absolute; /* 절대 위치 */
    top: 1%; /* 상단에 위치 */
    left: 50%; /* 화면의 가로 중앙에 위치 */
    transform: translateX(-50%); /* X축으로 -50% 이동하여 정확한 중앙 정렬 */
    z-index: 1000; /* 다른 요소들 위에 표시 */
    text-align: center; /* 텍스트 중앙 정렬 */
    width: 70%;
  }
  .logo img{
    width: 100%;
    height: auto;
  }

  .mission {
    top: 9%;
    z-index: 1000;
    width: 30%;
    height: 30%;
    position: relative; /* mission 요소 내에서 mission-current의 위치를 결정하기 위해 relative 설정 */
  }

  .mission img {
    width: 100%;
    height: auto;
  }

  .mission-current {
    position: absolute; /* mission 요소 내에서 절대 위치 설정 */
    top: 20%; 
    left: 35%;
    transform: translate(-50%, -50%); /* 정확한 중앙 정렬을 위해 */
    z-index: 1000; /* 이미지 위에 오도록 z-index 설정 */
    font-size: 20px; /* 폰트 크기 */
    color: black; /* 폰트 색상 */
  }
  .my-location-button {
    z-index: 1001;
    position: absolute;
    top: 25%;
    left: 5%;
    padding: 0px;
    border-radius: 3px;
    text-align: center;
  }

</style>