<template>
    <div class="final-page">
      <button @click="$router.push({name:'MainView'})" class="close ma-2 pa-2">
        <img src="@/assets/mission/close.png">
      </button>
      <div class="photo">
        <img id="displayImage" alt="photo">
      </div>
      <div class="present">
        <img :src="require('@/assets/open-present.png')">
      </div>
      <div class="button-container">
        <v-btn @click="downloadImage" class="ok-btn mt-3 pl-10 pr-10" color="#EF8200">다운로드</v-btn>
        <v-btn @click="openGoogleForm" class="google-form-button mt-3 pl-10 pr-10" color="#EF8200">만족도 설문조사 하기</v-btn>
      </div>
    </div>
    
</template>
  
<script>
export default {
  name: 'FinalView',
  data(){
    return {
      familyphoto:null,
    };
  },
  mounted() {
    let familyphotos = sessionStorage.getItem('displayphoto')
      // 예: 이미지 태그의 src 속성으로 설정
    document.getElementById('displayImage').src = familyphotos;
  },
  methods: {
    addphotoDataUrl(photoDataUrl) {
      this.familyphoto = photoDataUrl;
      console.log("familyphoto updated: ", this.familyphoto);
    },
    downloadImage() {
      
      },
      openGoogleForm(){
        const url = "https://docs.google.com/forms/d/e/1FAIpQLSdBCQgSi7xSaxSddm6OTSFwxXKcOjrNvLxfllJq-o0S7_09OQ/viewform?usp=sf_link";
        const options = "width = 700, height=600, left=200, top=200";
        window.open(url, "_blank", options);
      },
  },
  }

</script>
  
<style scoped>
  .final-page{
    background-image: url('@/assets/background.png');
    background-size: cover; /* 이미지가 div를 전체적으로 커버하도록 설정 */
    height: 100vh; /* 또는 다른 고정된 높이 */
    display: flex;
    justify-content: center; /* 가로 중앙 정렬 */
    align-items: center; /* 세로 중앙 정렬 */
    position: relative;
  }
  .close img{
    width: 22px;
    height: 22px;
    cursor: pointer;
    position: absolute;
    top: 3%;
    right: 5%;
  }

  .photo {
    position: absolute;
    width: 85%;
    height: auto;
    top: 10%;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .photo img{
    max-width: 100%;
    max-height: auto;

  }
  .present{
    position: absolute;
    bottom: 18%;
    width: 100%;
    left: 7%;
    height: auto;
  }
  .present img{
    width: 100%;
    height: 100%;
    /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); */
  }
  .button-container{
    position: absolute;
    bottom: 3%;
    display: flex; /* Flexbox 레이아웃 사용 */
    flex-direction: column; /* 요소들을 세로로 정렬 */
    align-items: center; /* 가로 중앙 정렬 */
  }

  .ok-btn, .google-form-button {
    color: white !important;
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 10px; /* 버튼 사이의 간격 */
    width: 80%;
  }

</style>