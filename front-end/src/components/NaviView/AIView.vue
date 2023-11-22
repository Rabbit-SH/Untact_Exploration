<template>

  <div class="main">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <button @click="$router.push({name:'MainView'})" class="closeAI ma-2 pa-2">X</button>
    <div class = "background">
      <img :src="require('@/assets/translate_img/aiPainter_head.png')">
    </div>
    <div class = "container">
      <img v-if="imageUrl" :src="imageUrl" alt="preview Image">
    </div>
     <v-overlay :value="loading">
      
      <v-card-text>
        수묵화 변환중...
        <v-progress-linear
          indeterminate
          color="white"
          class="mb-0"
        ></v-progress-linear>
      </v-card-text>
    </v-overlay>
    <div class="bt-container">
      <input type = "file" @change="uploadImg" class='input' ref="fileInput" style="display: none;" />
      <img :src="require('@/assets/translate_img/selectImg_bt.png')" @click= "triggeruploadImg">
      <br>
      <img v-if="istranslated" :src="require('@/assets/translate_img/btn_download.png')" @click="downloadImage">
      <img v-else :src="require('@/assets/translate_img/translateImg_bt.png')" @click= "transformImg">
    </div>
  </div>
</template>
<style scoped>
.main{
  height :100%;
  background-color: #F5F9EF;
}
.background{
  display: flex;
  align-items: center;
  justify-content: center;

}
.background img{
  width: 100%;
  height: 100%;
}
.container{
  background-image: url('~@/assets/translate_img//aiPainter_container.png');
  background-repeat: round;
  background-size: cover;
  height: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container img{
  width: 80%;
  height: 80%;
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
  width: 170px;  /* 원하는 너비로 설정 */
  height: 50px;
}
.bt-container{
  width: 100%;
  display: flex;
  flex-direction: column; /* 세로로 배치 */
  align-items: center; /* 가운데 정렬 */
}
</style>
<script>
import { EventBus } from '@/assets/EventBus';
import axios from 'axios';
export default {
  name: 'AIView',
  mounted() {
    EventBus.$on('add-photo',this.addphoto);
    window.addEventListener('beforeunload',this.beforeUnload);
  },
  beforeDestroy() {
    window.removeEventListener('beforeunload',this.beforeUnload)
    EventBus.$off('add-photo',this.addPhoto);
  },
  data() {
    return {
      preimage: null,
      loading: false,
      imageUrl:null,
      error:null,
      errorMessage: '',
      istranslated: false,
    }
  },
  methods: {
    triggeruploadImg(){
      this.$refs.fileInput.click();
    },
      beforeUnload(event) {
          // 이벤트 취소 메시지 설정
          event.preventDefault();
          event.returnValue = ''; // 대부분의 브라우저에서는 이 메시지가 표시되지 않습니다.
      },
    async uploadImg(event) {
      // 이미지 업로드 로직
      //만약 사진을 고르지 않았다면?
      this.imageUrl = null;
      this.preimage = event.target.files[0];
      if (!this.preimage) {
          console.log("파일을 선택해주세요.");
          return;
      }
      const fileReader = new FileReader();
      fileReader.readAsDataURL(this.preimage)
      fileReader.onload = () => {
              this.imageUrl = fileReader.result;
              // EventBus.$emit('add-photo', this.photoDataUrl);
          }
      this.istranslated = false

    },
    async transformImg() {
      // 이미지 변환 페이지로 이동하는 함수
      if (!this.preimage) {
        alert("사진을 선택해주세요!")
        return;
      }

      // 서버로 전송 하는 로직.
      const formData = new FormData();
      formData.append("file", this.preimage);

      this.loading = true;
      this.error = false;
      this.errorMessage = '';

      try {
          this.response = await axios.post('https://5e11-1-244-138-205.ngrok.io:8000/upload', formData,{responseType: 'blob'});
          
          this.imageUrl = URL.createObjectURL(this.response.data);
          // console.log("변환된 이미지 URL:", this.imageUrl);
          this.loading = false;
      } catch (error) {
          console.error("Error during image processing:", error);
          this.error = true;
          this.errorMessage = 'Error processing image. Please try again.';
          this.loading = false;
      }
      this.istranslated = true;

    },
    downloadImage() {
      const link = document.createElement('a');
          link.href = this.imageUrl;
          link.download = 'stylized_image.jpg';  // 다운로드될 파일명 설정
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          this.istranslated = false
    }
  }
}
</script>