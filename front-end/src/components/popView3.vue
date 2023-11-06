<template>
  <div class="black-bg" v-if="show">
    <div class="white-bg"> 
      <button class="close" @click="closeP">X</button>
        <h4> 3지선다 문제</h4>
        <p> 문제를 맞춰보쇼 </p>
      <div class="Question">
      <div>
        <input type="radio" id="1" value="A1" v-model="userResponse">
        <label for="1">1. 혜원</label>
      </div>
      <div>
        <input type="radio" id="2" value="A2" v-model="userResponse">
        <label for="2">2. 민정</label>
      </div>
      <div>
        <input type="radio" id="3" value="A3" v-model="userResponse">
        <label for="3">3. 수현</label>
      </div>
      <div>
        <input type="radio" id="4" value="A4" v-model="userResponse">
        <label for="4">4. 진우</label>
      </div>
      <div>
        <input type="radio" id="5" value="A5" v-model="userResponse">
        <label for="5">5. 기문</label>
      </div>
    </div> 
      <div class="button-container">
          <button class="submit" @click="submitResponse">제출하기</button>
          <button class="hint" @click="showHint">힌트</button>
      </div>
      <div class="hint-popup" v-if="showPopup">
              <button class="close-popup" @click="closePopup">X</button>
              <!-- <p> 힌트 팝업창</p>
              <br> -->
              <h1> 김민정이다 이 자식들아! </h1>
              <p>젤 이쁜애자나~~</p>
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
        result3:{
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
        //팝업 여는 메소드
        showHint(){
          this.showPopup=true;
        },
        //팝업 닫는 메소드
        closePopup(){
          this.showPopup=false;
        },
        submitResponse() {
          if (this.userResponse.trim() === '') {
              alert("답변을 입력해주세요!");
          } else {
              // Check if the answer is correct
              if (this.userResponse === 'A2') {
                  alert("정답입니다!");
                  this.userResponse = ''; // 답변이 제출되면 리셋하기
                  this.closeP();
              } else {
                  alert("다시 한번 더 읽어볼까요?!");
              }
          }
      },
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