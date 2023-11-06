<template>
  <div class="black-bg" v-if="show">
    <div class="white-bg">
      <button class="close" @click="closeP">X</button> 
        <h4> 쉿! 가만히 앉아 눈을 감아요</h4>
          <p> 60초 동안 주변 소리에 귀 기울여 볼까요? </p>
          <p> 어떤 소리가 들리나요? </p>
          <p> 들리는 소리를 글로 표현해 적습니다 </p>
          <p> 예) 째액째액, 까악까악, 윙윙 </p>
          <br>
          <br>
        <figure>
          <figcaption>새소리를 들어보세요!!!</figcaption>
          <audio controls src="@/assets/99941F4C5CF91EAC0F.mp3">
              <a href="@/assets/99941F4C5CF91EAC0F.mp3">Download audio</a>
          </audio>
      </figure>
      <textarea class="text" v-model="userResponse" placeholder="여기에 소리를 표현해보세요..."></textarea>
      <div class="button-container">
          <button class="submit" @click="submitResponse">제출하기</button>
          <button class="hint" @click="showHint">힌트</button>
      </div>
      <div class="hint-popup" v-if="showPopup">
              <button class="close-popup" @click="closePopup">X</button>
              <p> 힌트 팝업 페이지 </p>
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

<style>
    body{
        margin: 0;
    }
    div{
        box-sizing: border-box;
    }
    .black-bg{
        width: 100%; height: 100%;
        background: rgba(0, 0, 0, 0.5);
        position: fixed; padding: 20px;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .white-bg{
        width: 80%; height: 80%; 
        background:white;
        border-radius: 8px;
        padding: 50px;
        overflow: scroll;
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
      margin-top: 20px;
      padding: 10px;
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
      display: flex;
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