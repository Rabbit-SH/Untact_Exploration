<template>
  <div class="black-bg" v-if="show">
    <div class="white-bg">
      <button class="close" @click="closeP">X</button> 
        <br>
      <div class="br"></div>
      <figure>
        <!-- <figcaption>새소리를 들어보세요!!!</figcaption> -->
        <audio controls src="@/assets/99941F4C5CF91EAC0F.mp3">
          <a href="@/assets/99941F4C5CF91EAC0F.mp3">Download audio</a>
        </audio>
      </figure>
      <br>
      <textarea class="text" v-model="userResponse" placeholder="여기에 소리를 표현해보세요..."></textarea>
      <div class="button-container">
        <button class="submit" @click="submitResponse">제출하기</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    props: {
        show: {
            type: Boolean,
            required: true,
        },
        result2:{
          type: Boolean,
          // default: false,
        }
    },
    data(){
      return {
          userResponse: '', //사용자 응답 저장하는 데이터
          showPopup: false, //팝업 상태
      }
    },
    methods: {
        closeP(){
            this.$emit('close');
        },
        submitResponse(){
          if(this.userResponse.trim() !== ''){
            console.log(this.userResponse); //콘솔에 출력, 서버에 제출하거나 다른 제출을 추가해도됨
            this.userResponse = ''; //답변이 제출되면 리셋하기

            // 사용자에게 사진이 제출되었다는 알림
            alert("답변이 제출되었습니다.");
            if(this.result2 == false) {
              this.$emit('answerCorrect')
              console.log('pop2에서는 정상적으로 이벤트 호출함')
            }

            // 팝업 닫기
            this.closeP();
          }
          else{
            // 답변이 제출되지 않았다는 알림창
            alert("답변을 입력해주세요!");
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
          background-image: url('~@/assets/background_pop2.png');
          background-size: contain;
          background-position: center; /* 이미지를 중앙에 정렬합니다 */
      }

    figure {
      margin: 0;
    }
    .text{
      display: flex;
      justify-content: center; /* 수평 중앙 정렬*/
      align-items: center; /* 수직 중앙 정렬*/
    }
    textarea{
      margin: auto;
      width: 90%;
      height: 100px;
      /* margin-top: 60%; */
      /* bottom: 20%; */
      padding: 10px;
      /* justify-content: center; */
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
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
    .button-container{
      /* display: flex; */
      position: absolute; /* 고정 위치 */
      /* bottom: 50%; 하단에 위치 */
      left: 0; /* 왼쪽에 위치 */
      bottom: 3%;
      width: 100%; /* 너비를 전체로 설정 */
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
    audio{
      display:inline-block;
      vertical-align: middle;
      align-items: center;
      /* padding-left: 15px; */
      padding-right: 10px;
      margin-right: 0;
      /* width: 250px; */
    }
    .br{
      height: 40%;
      display:inline-block;
    }
    figure{
      align-items: center;
    }

</style>