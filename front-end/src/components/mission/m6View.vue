<template>
    <div class="black-bg" v-if="show">
        <div class="white-bg">
            <button class="close" @click="closeP">
                <img src="@/assets/mission/close.png">
            </button>
            <div class="content">
                <div class="cam-container">
                    <div @click="triggerCamera" class="cam-button mb-3">
                        <svg-icon type="mdi" :path="path"></svg-icon>
                    </div>
                    <input type="file" name="photofile" id="photofile" accept="image/*" capture="camera"
                    @change="onPhotoFileChange">
                </div>
                <br>
                <div class="img-container text-center">
                    <img src="" id="photoimg">
                </div>
                <div class="button-container">
                    <v-btn class="custom-submit-button mt-3 pl-10 pr-10" color="#EF8200" @click="submitSoundRes">제출하기</v-btn>
                </div>
            </div>
        </div>
        <v-dialog v-model="dialog" max-width="500">
            <v-card class="pa-3">
                <v-card-text>
                <v-row align="center" justify="center">
                    <v-col align="center">
                    <div class="img-container text-center">
                        <img :src="uploadedPhoto" id="dialogPhoto" style="max-height:100%; max-width:100%;">
                    </div>
                    <br>
                    <div class="text-center">
                        <p>이미지 다운로드를 원하면 아래의 <strong>다운로드</strong> 버튼을 눌러주세요.</p>
                        <p>내가 찍은 사진을 수묵화 그림으로 바꿔보고 싶다면 <strong>AI 화가</strong> 버튼을 눌러주세요.</p>
                    </div>
                    <div>
                        <div class="btn_container">
                            <v-btn @click="downloadImage(uploadedPhoto)" class="mr-3">다운로드</v-btn>
                            <v-btn @click="goToAiPainter" class="ml-3">AI 화가</v-btn>
                        </div>
                        <div>
                            <v-btn @click="handleDialogConfirmation" class="mt-3" color="primary">다음 미션으로</v-btn>
                        </div>
                    </div>
                    </v-col>
                </v-row>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
</template>

<script >
import EventBus from '@/EventBus.js';
import SvgIcon from '@jamescoyle/vue-icon';
import { mdiCameraOutline } from '@mdi/js';

export default {
    props: {
        show: {
            type: Boolean,
            required: true,
        },
        result4: {
            type: Boolean,
        }
    },
    components:{
        SvgIcon
    },
    data(){
      return {
        userResult: '', //사용자 응답 저장하는 데이터
        dialog: false,

        userResponse:'',
        uploadedPhoto: null, // 업로드된 사진 데이터를 위한 변수

        path: mdiCameraOutline,
      }
    },
    methods: {
        closeP(){
            this.$emit('close');
        },
        triggerCamera(){
            const photoFileInput = this.$el.querySelector("#photofile");
            photoFileInput.click();
        },
        onPhotoFileChange(event){
            let filename;
            if (window.FileReader) {
                filename = event.target.files[0].name;
            } else {
                filename = event.target.value.split('/').pop().split('\\').pop();
            }
            console.log("파일 사이즈 : " + event.target.files[0].size);
            console.log("파일명 : " + filename);
  
            this.previewImage(event.target);
  
              // 업로드된 파일 데이터를 저장합니다.
            this.uploadedPhoto = event.target.files[0];

              // 파일데이터를 갤러리 리스트에 추가합니다.
            const fileReader = new FileReader();
            fileReader.readAsDataURL(event.target.files[0]);
            fileReader.onload = () => {
                // const photoDataUrl = fileReader.result;
                // EventBus.$emit('add-photo', photoDataUrl);
                const photoDataUrl = fileReader.result;
                this.uploadedPhoto = photoDataUrl;
                EventBus.$emit('add-photo', photoDataUrl);
            }
        },
        previewImage(inputElement){
            if (inputElement.files && inputElement.files[0]) {
                let reader = new FileReader();
                reader.onload = (e) => {
                    this.$el.querySelector("#photoimg").setAttribute('src', e.target.result);
                    this.$el.querySelector("#photoimg").style.display = "block";
                }
                reader.readAsDataURL(inputElement.files[0]);
            }
        },
        submitResponse(){
            // 사진이 업로드되었는지 확인
            if (this.uploadedPhoto) {
                console.log(this.userResponse); // 콘솔에 출력
                this.userResponse = ''; // 답변 리셋

                this.dialog = true;

            } else {
                // 사진이 업로드되지 않았다면 경고 알림
                alert("사진을 찍어주세요!");
            }
        },
        handleDialogConfirmation(){
            this.dialog = false;

            if (this.result4 === false){
                this.$emit('answerCorrect');
            }
            this.userResult = ''; // 사용자 응답 리셋
            this.closeP();        // 다이얼로그 닫기
        },
        goToAiPainter(){
            this.$router.push({name:'AIView'});
            if (this.result4 === false){
                this.$emit('answerCorrect');
            }
            this.userResult = '';
            this.closeP();

        },

        downloadImage(uploadedPhoto) {
            if (uploadedPhoto) {
                // 이미지를 다운로드하는 링크를 생성
                const a = document.createElement('a');
                a.href = uploadedPhoto;

                // 다운로드되는 파일의 이름 설정 (예: downloaded-image.jpg)
                const filename = `family_img`;
                a.download = filename;

                // 링크를 추가하고 클릭하여 다운로드 시작
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            } else {
                // 이미지가 없는 경우에 대한 처리 (예: 경고 또는 사용자에게 알리기)
                alert('이미지를 먼저 업로드하세요!');
            }
        },

    }
}
</script>

<style scoped>
    .black-bg{
        width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.5);
        position: fixed; 
        top: 0;
        left: 0;
        padding: 20px;
        z-index: 1500;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .white-bg{
        width: 90%; height: 90%;
        border-radius: 22px;
        position: fixed; 
        /* background-color: white; */
        overflow:hidden;
        display:flex;
        flex-direction: column; 
        align-items: flex-end;
        background-image: url('@/assets/mission/bg_6.png');
        background-size: cover; /* 배경 이미지 크기 조정 옵션 */
        background-position: center; /* 배경 이미지 위치 조정 옵션 */
        background-repeat: no-repeat; /* 배경 이미지 반복 설정 */
      }
    .content{
        width:100%;
        position: absolute;
        bottom: 7%;
        max-height: 50%;
        overflow-y: auto;
    }
    .close img{
        width: 22px;
        height: 22px;
        cursor: pointer;
        justify-content: center;
        align-items: center;
        position:absolute;
        top: 3%;
        right: 5%;
    }
    .img-container{
        justify-content: center;
        display: flex;
        align-items: center;
    }
    #photoimg {
        display: none;
        width: 70%;
        height: auto; /* 이미지의 원래 비율을 유지 */
        margin-top: 20px; /* 상단 여백 추가 */
    }
    #photofile{
        display:None;
        /* background: yellow; */
        /* height: 50%; */
        /* width: auto; */
    }
    #dialogPhoto {
        width: 80%; /* 이미지 크기 조절 */
    }
    .cam-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px; /* 상단 여백 추가 */
    }
    .button-container {
        width: 100%; /* 너비를 전체로 설정 */
        padding: 10px 20px; /* 패딩을 상하에만 적용 */
        display: flex; /* 버튼들을 가로로 정렬 */
        justify-content: center; /* 가운데 정렬 */
        margin-top: auto; /* 위쪽 요소들이 차지한 후 남은 공간을 모두 차지 */
    }
    .custom-submit-button {
        color: white !important; /* 텍스트 색상을 흰색으로 */
        font-weight: bold; /* 글씨 두께를 굵게 */
        font-size: 18px; /* 글씨 크기를 18px로 설정 */
    }
</style>