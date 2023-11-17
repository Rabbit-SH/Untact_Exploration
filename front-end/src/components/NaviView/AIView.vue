<template>
    <div class="main">
      <v-btn @click="$router.push({name:'MainView'})" class="closeAI ma-2 pa-2">X</v-btn>
  
      <div class="bt-container">
        <!-- <v-btn class="upload_img"> 사진 선택 </v-btn>
        <v-btn class="korea_paint"> 수묵화로 변환 </v-btn> -->
        <img :src="require('@/assets/translate_img/selectImg_bt.png')">
        <img :src="require('@/assets/translate_img/translateImg_bt.png')">
      </div>
  
    </div>
  </template>
  
  <script>
  export default {
    name: 'AIView'
  
  }
  </script>
  
  <style>
    .main{
      /* background-color: yellow; */
      background-image: url('~@/assets/translate_img/aiPainter.png');
      background-repeat: None;
      background-size: contain;
      background-position: center;
      height :100%;
      width: 100%
    }
  
    .closeAI {
      position: absolute; /* 절대 위치 설정 */
      top: 0; /* 맨 위로 이동 */
      right: 0; /* 맨 오른쪽으로 이동 */
      height : 10px;
      width: 10px;
    }
    .upload_img{
      background-color: '#F7EAA1';
    }
    .korea_paint{
      background-color: '#F7EAA1';
    }
    .bt-container img{
      width : 55%;
      height: auto;
      margin: 2%;
    }
    .bt-container{
      display: flex;
      flex-direction: column; /* 세로로 배치 */
      align-items: center; /* 가운데 정렬 */
      margin-top: 10%; /* 버튼 컨테이너 상단 여백 조절 */
      position: absolute;
      bottom: 13px;
    }
  </style>