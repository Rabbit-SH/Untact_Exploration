<template>
    <div class="black-bg" v-if="show">
        <div class="white-bg">
            <button class="close" @click="closeP">X</button> 
                <div class="br" />
                <div clas="soundDiv">
                    <div class="sound">
                        <input type="radio" name="bird_sound" value="꿩" v-model="userResult" checked="checked">
                        <audio controls src="@/assets/꿩.wav"></audio>
                    </div>
                    <br>
                    <div class="sound">
                        <input type="radio" name="bird_sound" value="참새" v-model="userResult">
                        <audio controls src="@/assets/99941F4C5CF91EAC0F.mp3"></audio>
                    </div>
                    <br>
                    <div class="sound">
                        <input type="radio" name="bird_sound" value="비둘기" v-model="userResult">
                        <audio controls src="@/assets/비둘기.wav"></audio>
                    </div>
                </div>
                <br>
                <div class="button-container">
                    <button class="submit" @click="submitSoundRes">제출하기</button>
                </div>
        </div>
    </div>
</template>

<script >
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
    data(){
      return {
          userResult: '', //사용자 응답 저장하는 데이터
          showPopup: false, //팝업 상태
      }
    },
    methods: {
        closeP(){
            this.$emit('close');
        },
        submitResponse(){
          console.log(this.userResponse); //콘솔에 출력, 서버에 제출하거나 다른 제출을 추가해도됨
          this.userResponse = ''; //답변이 제출되면 리셋하기
        },
        //팝업 여는 메소드
        showHint(){
          this.showPopup=true;
        },
        //팝업 닫는 메소드
        closePopup(){
          this.showPopup=false;
        },
        submitSoundRes () {
          if (this.userResult.trim() === '') {
              alert("답변을 입력해주세요!");
          } else {
              // Check if the answer is correct
              if (this.userResult === '꿩') {
                  alert("정답입니다!");
                  if(this.result4 == false) {
                    this.$emit('answerCorrect')
                  }
                  this.userResult = ''; // 답변이 제출되면 리셋하기
                  this.closeP();
              } else {
                  alert("다시 한번 들어볼까요?!");
              }
          }
        },

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
          background-image: url('~@/assets/background_pop4.png');
          background-size: contain;
          background-position: center; /* 이미지를 중앙에 정렬합니다 */
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
    .sound {
        white-space: nowrap; /*줄바꿈 방지해 한 줄에 표시*/
    }
    .sound input[type="radio"],
    .sound audio {
        display:inline-block;
        vertical-align: middle;
        padding-left: 15px;
        padding-right: 0px;
        margin-right: 0;
        /* width: 250px; */
    }
    .button-container{
      /* display: flex; */
      position: absolute; /* 고정 위치 */
      /* bottom: 50%; 하단에 위치 */
      left: 0; /* 왼쪽에 위치 */
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
    .br{
        display:inline-block;
        height: 50%;
    }
</style>