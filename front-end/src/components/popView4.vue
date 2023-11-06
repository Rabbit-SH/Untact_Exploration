<template>
    <div class="black-bg" v-if="show">
        <div class="white-bg">
            <div class="closebuttonDiv">
                <button class="close" @click="closeP">X</button> 
            </div>
            <div class="content">
                <div class="explainProblem">
                    <h4>쉿! 가만히 앉아 눈을 감아보세요.</h4>
                    <p>60초 동안 주변 수리에 귀 기울여 볼까요?</p>
                    <p>새들이 지저귀는 소리가 들리나요?!</p>
                    <br>
                    <p> 꿩은 울 때 꿩- 하고 울어서 이름이 꿩이랍니다.</p>
                    <p> 다음 중 어떤 소리가 꿩의 소리인지 찾아보세요!</p>
                    <br>
                </div>
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
                <div class="buttonDiv">
                    <button class="submit" @click="submitSoundRes">제출하기</button>
                    <button class="hint" @click="showHint">힌트</button>
                </div>
                <div class="hint-popup" v-if="showPopup">
                    <button class="close-popup" @click="closePopup">X</button>
                    <p> 힌트 팝업 페이지 </p>
                </div>
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
        position: fixed;
        z-index: 1000;
        align-items: center;
        display: flex;
        justify-content: center;
    }
    .white-bg{
        width: 85%; height: 80%; 
        background:white;
        border-radius: 8px;
        margin: 0;
        padding:5px !important;
    }
    .closebuttonDiv{
        display:block;
        height: 5%;
        align-content: center;
    }
    .content{
        display:block;
        height: 95%;
        width: 100%;
        padding: 20px;
        background-color: yellow;
        border-radius: 0px;
        overflow: auto;
    }
    .close{
        padding: 10px;
        height:20px;
        width: 20px;
        justify-content: center;
        align-items: center;
        margin-left: auto;
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
    .buttonDiv{
        display:flex;
        padding: 10px;
        height: 65px;
        justify-content: center;
        width: 100%;
    }
    .buttonDiv button{
        padding: 10px;
        align-items: center;
    }
</style>