<template>
    <div class="black-bg" v-if="show">
      <div class="white-bg">
        <button class="close" @click="closeP">X</button> 
        <div class="content">
            <div align="center" justipy="center">
                <img src="" id="photoimg">
                <div class="content2">
                    <input type="file" name="photofile" id="photofile" accept="image/*" capture="camera"
                    @change="onPhotoFileChange">
                    <input type="button" value="잎 사진 찍기"
                    @click="triggerCamera" class="cam-button">
                </div>
            </div>
            <div class="button-container">
                <button class="submit" @click="submitResponse">제출하기</button>
            </div>
        </div>
        </div>

    </div>
  </template>
  
  <script>
    import EventBus from '@/EventBus.js';

  export default {
      props: {
          show: {
              type: Boolean,
              required: true,
          },
          result1:{
            type: Boolean,
            }
      },
      data(){
          return{
              showPopup:false,
              userResponse:'',
              uploadedPhoto: null, // 업로드된 사진 데이터를 위한 변수
          };
  
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
                const photoDataUrl = fileReader.result;
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

                // 사용자에게 사진이 제출되었다는 알림
                alert("사진이 제출되었습니다.");
                
                if(this.result1 == false) {
                this.$emit('answerCorrect')
                }

                // 팝업 닫기
                this.closeP();
                } 
            else {
                // 사진이 업로드되지 않았다면 경고 알림
                alert("사진을 찍어주세요!");
            }
        },
        //팝업 여는 메소드
        showHint(){
            this.showPopup=true;
        },
        //팝업 닫는 메소드
        closePopup(){
            this.showPopup=false;
        }
      }
  }
  
  </script>
  
  <style scoped>
      body{
          margin: 0;
      }
      div{
          box-sizing: border-box;
      }
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
          /* position: relative; */
          border-radius: 8px;
          position: fixed; 
          padding: 20px;
          overflow-y: auto;
          background-image: url('~@/assets/background_pop6.png');
          background-size: contain;
          background-position: center; /* 이미지를 중앙에 정렬합니다 */
      }

      .content{
          width: 90%; height: 90%;
          position: absolute;
          top: 50%;
          border-radius: 8px;
          overflow-y: auto;
          margin: 0 auto; /* 가운데 정렬 */
      }
      #photoimg{
          display:None;
          width: 30%; height: 30%; 
      }
      #photofile{
          display:None;
      }
      .cam-button{
          z-index: 1000;
          position: relative;
          margin: 0 auto; /* 가운데 정렬 */
          display: block;
      }
        .close{
            display: flex;
            width: 5%;
            padding: 10px 10px;
            margin-top: 5px;
            background-color: #ccc;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-left: auto; /* 왼쪽 마진을 오토로 설정해서 오른쪽으로 밀어냄 */
            justify-content: center;
        
      }
      .button-container {
          position: absolute; /* 고정 위치 */
          bottom: 50%; /* 하단에 위치 */
          left: 0; /* 왼쪽에 위치 */
          width: 100%; /* 너비를 전체로 설정 */
          bottom: 3%;
          background-color: #fff; /* 배경 색상 */
          padding: 10px 20px; /* 패딩을 상하에만 적용 */
          display: flex; /* 버튼들을 가로로 정렬 */
          justify-content: center; /* 가운데 정렬 */
          z-index: 10; /* 다른 요소들 위에 나타나도록 z-index 설정 */
      }
      .submit{
          flex: none;
          width: 80%;
          padding: 10px 10px;
          margin-top: 5px;
          background-color: #0056b3;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          justify-content: start;
        }
      .hint{
          flex: none;
          width: 20%;
          padding: 10px 10px;
          margin-top: 5px;
          background-color: #0056b3;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          margin-left: 10px;
        }
       
      button:hover{
          background-color: #0056b3;
        }
      .hint-popup{
          width: 65%; height: 65%;
          position:fixed;
          top: 50%;
          left: 50%;
          border-radius: 4px;
          transform: translate(-50%, -50%); /* 자신의 크기만큼 이동하여 완전히 중앙에 오도록 조정 */
          background: wheat;
          display: flex;
          align-items: center;
          justify-content: center;
          z-index: 2000;
        }
      .close-popup {
          position: absolute;
          top: 10px;
          right: 10px;
          display: flex;
          width: auto;
          padding: 10px 20px;
          margin-top: 5px;
          background-color: #ccc;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          margin-left: auto; /* 왼쪽 마진을 오토로 설정해서 오른쪽으로 밀어냄 */
        }
  
  
  </style>