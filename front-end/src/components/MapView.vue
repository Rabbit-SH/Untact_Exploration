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
    
    <v-app-bar
      app
      color="green"
      dark
      style="z-index: 1000"
      >
      <div class = "d-flex justify-center flex-grow-1">
          <span class="mr-2">물두꺼비를 따라가보자!</span>
      </div>
      <div class="mission">
        <img :src="require('@/assets/mission.png')" @click="getDurumari">
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
    </v-app-bar>

      <pop1 :show="popVal1" @close="closeP" @answerCorrect="updateResult(1)" class="popup" :class="{'show':popVal1}" />
      <pop2 :show="popVal2" @close="closeP" @answerCorrect="updateResult(2)" class="popup" :class="{'show':popVal2}" />
      <pop3 :show="popVal3" @close="closeP" @answerCorrect="updateResult(3)" class="popup" :class="{'show':popVal3}" />
      <pop4 :show="popVal4" @close="closeP" @answerCorrect="updateResult(4)" class="popup" :class="{'show':popVal4}" />
      <pop5 :show="popVal5" @close="closeP" @answerCorrect="updateResult(5)" class="popup" :class="{'show':popVal5}" />
      <pop6 :show="popVal6" @close="closeP" @answerCorrect="updateResult(6)" class="popup" :class="{'show':popVal6}" />

      <infoChiakView :show="showInfoChiak" class="infoChiak" :class="{'show': showInfoChiak}" @closeTutorial="closed"/>
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
        :icon="result2 ? customIcon: defaultIcon" />

      <LMarker
        :key="markers[2].id"
        :lat-lng="markers[2].coordinates"
        @click="openP(2)"
        :icon="result3 ? customIcon: defaultIcon" />

      <LMarker
        :key="markers[3].id"
        :lat-lng="markers[3].coordinates"
        @click="openP(3)"
        :icon="result4 ? customIcon: defaultIcon"></LMarker>

      <LMarker
        :key="markers[4].id"
        :lat-lng="markers[4].coordinates"
        @click="openP(4)"
        :icon="result5 ? customIcon: defaultIcon" />
      
      <LMarker
        :key="markers[5].id"
        :lat-lng="markers[5].coordinates"
        @click="openP(5)"
        :icon="result6 ? customIcon: defaultIcon" />

      <LMarker
        :key="markers[6].id"
        :lat-lng="markers[6].coordinates"
        :icon="defaultIcon" />

      <LMarker
        :key="markers[7].id"
        :lat-lng="markers[7].coordinates"
        :icon="defaultIcon" />

      <LMarker
        :key="markers[8].id"
        :lat-lng="markers[8].coordinates"
        :icon="defaultIcon" />

      <LMarker
        :key="markers[9].id"
        :lat-lng="markers[9].coordinates"
        :icon="defaultIcon" />

      <LMarker
        :key="markers[10].id"
        :lat-lng="markers[10].coordinates"
        :icon="defaultIcon" />

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
                @click="getDurumari" 
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


      <!-- <div @click="InfoChiak" class="chiakInfo">
        <img :src="require('@/assets/reward_a.png')">
      </div> -->

      <div  class="animated-marker" v-show="isGift">
        <img :src="require('@/assets/present.png')">
      </div>

    </l-map>
  </div>
</template>
   
<script>
import { LMap, LTileLayer, LMarker, LCircle } from 'vue2-leaflet';
import L from 'leaflet';
import { Icon } from 'leaflet';

import EventBus from '@/EventBus.js';

import pop1 from '../components/popView/popView1.vue';
import pop2 from '../components/popView/popView2.vue';
import pop3 from '../components/popView/popView3.vue';
import pop4 from '../components/popView/popView4.vue';
import pop5 from '../components/popView/popView5.vue';
import pop6 from '../components/popView/popView6.vue';

import infoChiakView from '../components/NaviView/InfoChiakView.vue';
import GiftView from '../components/GiftView.vue';

import 'leaflet/dist/leaflet.css';
import 'leaflet-gpx';

import markerImg from 'leaflet/dist/images/marker-icon.png';
import markerShadowImg from 'leaflet/dist/images/marker-shadow.png';
import markerRetinaImg from 'leaflet/dist/images/marker-icon-2x.png';

import Durumari from './NaviView/DurumariView.vue';
import GalleryView from './NaviView/GalleryView.vue';
import TutorialView from './NaviView/TutorialView.vue';
import UploadImageView from './/NaviView/UploadImageView2.vue';


export default {

  data () {
    return {
      // url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      // attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      url: 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
      attribution: '&copy; <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> '
                    + '&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors',
      // center: [ 37.40436362096728, 128.0495492913938], // 처음 지도의 중심이 되는 좌표 / 각 포인트들의 중점
      // center: [37.4148911042466, 128.05010676384],
      // center:[37.405103579156, 128.04869055748],
      center: [37.4014687, 128.049426499],
      zoom: 15, // 초기 확대 레벨
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

      result1: false,
      result2: false,
      result3: false,
      result4: false,
      result5: false,
      result6: false,

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
        {id:1, coordinates: [37.4045112586344, 128.047172427177], name:'시작 지점'},
        {id:2, coordinates: [37.4047243241094, 128.04743796587], name:'황장금표'},
        {id:3, coordinates: [37.40485112, 128.04897584], name:'황장숲목길 시작'},
        {id:4, coordinates: [37.40344835, 128.04888571], name:'가족사진 미션(후보)'},
        {id:5, coordinates: [37.3994891299528, 128.049967288971], name:'구룡사 사진미션 장소'},
        // {id:6, coordinates: [37.39832721, 128.05118929], name:'출렁다리 이후 잎 비교 미션'},
        {id:7, coordinates: [37.3972602794003, 128.051370084286], name:'꿩 전설(범람로 시작)'},
        {id:8, coordinates: [37.39634559, 128.05203636], name:'나무 잎 비교 미션'},
        {id:9, coordinates: [37.3962438504021, 128.051914572716], name:'솔방울 줍기 미션'},
        {id:10, coordinates: [37.395769, 128.052579], name:'갈림길 합쳐지는 곳'},
        {id:11, coordinates: [37.3943047128225, 128.053515851498], name:'종료 지점'},
        {id:12, coordinates: [37.394792698322, 128.053207397461], name:'히든미션(금강초롱꽃을 찾아라)'},        

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
    pop1,
    pop2,
    pop3,
    pop4,
    pop5,
    pop6,
    infoChiakView,
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
        },
        closeGallery(){
            this.gallery_open = false;
            this.isCredit = false;
            this.showtutorial = false;
            this.uploadIMG = false;
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
    closeP(){
      this.popVal1 = false;
      this.popVal2 = false;
      this.popVal3 = false;
      this.popVal4 = false;
      this.popVal5 = false;
      this.popVal6 = false;
      
      // 지도의 드래그와 스크롤 줌 활성화
      if (this.$refs.map && this.$refs.map.mapObject) {
      this.$refs.map.mapObject.dragging.enable();
      this.$refs.map.mapObject.scrollWheelZoom.enable();
    }

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
      // const gpxUrl = process.env.BASE_URL + '치악산 탐방서비스 등산로.gpx'
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
      this['result' + (id)]=true;
      const results = {
        r1: this.result1,
        r2: this.result2,
        r3: this.result3,
        r4: this.result4,
        r5: this.result5,
        r6: this.result6,
      };
      EventBus.$emit('send-results-to-durumari', results);
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

      this.isGift = true;
    },
    Good(){
      this.result1 = true;
      this.result2 = true;
      this.result3 = true;
      this.result4 = true;
      this.result5 = true;
      this.result6 = true;
    }
  },
  computed:{
    allRes(){
      return [this.result1, this.result2, this.result3, this.result4, this.result5, this.result6].every(Boolean);
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
  .mission{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 35%; 
    height: 35%; 
    position: absolute;
    left: 15%;
    top: 100%;
    transform: translate(-50%, -50%); /* 중앙에서 정확히 위치하도록 조정 */
  }
  .mission img{
    width: 100%;
    height: auto;
  }
  .my-location-button {
    z-index: 1001;
    position: absolute;
    top: 100px;
    left: 10px;
    padding: 0px;
    border-radius: 3px;
    text-align: center;
  }
  .location-button-red {
    filter: grayscale(100%);
    z-index: 1001;
    position: absolute;
    bottom: 90px;
    left: 10px;
    width: 30px;
    height: 30px;
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
  bottom: 5%; /* 화면 하단 */
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

</style>
