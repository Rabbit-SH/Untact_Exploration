<template>
    <div class="final-page">
      <div class="photo">
        <img :src="require('@/assets/photo.jpeg')">
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
  import EventBus from '@/EventBus.js';

  export default {
    name: 'FinalView',
    data(){
      return {
        familyphoto:'',
      };
    },
    created() {
      EventBus.$on('add-family-photo', this.addphotoDataUrl);
      console.log("familyphoto updated: ", this.familyphoto);
    },
    methods: {
      addphotoDataUrl(photoDataUrl) {
        this.familyphoto = photoDataUrl;
        
      },
      downloadImage() {
        const imageUrl = require('@/assets/photo.jpeg');
          // Blob 객체를 생성합니다.
          fetch(imageUrl)
            .then(res => res.blob())
            .then(blob => {
              // Blob 객체를 이용하여 다운로드 링크를 생성합니다.
              const blobUrl = window.URL.createObjectURL(blob);
              const link = document.createElement('a');
              link.href = blobUrl;
              link.download = 'downloaded-image.jpeg'; // 다운로드될 파일 이름

              // 링크를 문서에 추가하고 클릭 이벤트를 트리거합니다.
              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);

              // Blob URL을 해제합니다.
              window.URL.revokeObjectURL(blobUrl);
            })
            .catch(err => console.error(err));
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

    .photo {
      position: absolute;
      width: 85%;
      height: auto;
      top: 10%;
    }

    .photo img{
      max-width: 100%;
      max-height: auto;
    }
    .present{
      position: absolute;
      bottom: 15%;
      width: 100%;
      left: 7%;
      height: auto;
    }
    .present img{
      width: 100%;
      height: 100%;
    }
    .button-container{
      position: absolute;
      bottom: 10%;

    }
    .ok-btn {
        color: white !important; /* 텍스트 색상을 흰색으로 */
        font-weight: bold; /* 글씨 두께를 굵게 */
        font-size: 18px; /* 글씨 크기를 18px로 설정 */
        margin-right: 5px;
    }
    .google-form-button {
        color: white !important; /* 텍스트 색상을 흰색으로 */
        font-weight: bold; /* 글씨 두께를 굵게 */
        font-size: 18px; /* 글씨 크기를 18px로 설정 */
    }

  </style>