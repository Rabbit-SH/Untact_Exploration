<template>
    <div class="black-bg" v-if="show">
        <div class="white-bg">
            <img :src="require('@/assets/mission/bg_1.png')">

            <button class="close" @click="closeP">X</button>
            <div class="content-container" justify="center" align="center">
                
                <div class="soundDiv">
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
                <v-btn color="primary" class="text-center mt-3 pl-10 pr-10" @click="submitSoundRes">제출하기</v-btn>
            </div>
        </div>
        <v-dialog v-model="dialog" max-width="500">
            <v-card>
                <v-card-text>
                    <v-row align="center" justify="center">
                        <v-col align="center">
                            <div style="height:70%; width:70%; display: flex; align-items: center; justify-items: center;">
                                <v-img v-if="userResult === '꿩'" src="@/assets/O.png" style="max-height:100%; max-width:100%;"></v-img>
                                <v-img v-else src="@/assets/X.png" style="max-height:100%; max-width:100%;"></v-img>
                            </div>
                            <br>
                            <div v-if="userResult === '꿩'" class="text-center">
                                <h3>정답입니다!</h3> 
                                <h4>확인 버튼을 눌러주세요.</h4>
                            </div>
                            <div v-else class="text-center">
                                <h3>다시 한번 풀어볼까요?</h3>
                            </div>
                        </v-col>
                    </v-row>
                </v-card-text>
                <v-card-actions>
                <v-btn @click="handleDialogConfirmation(userResult === '꿩')" class="ml-auto">확인</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script scoped>
export default {
    props: {
        show: {
            type: Boolean,
            required: true,
        },
        result1: {
            type: Boolean,
        }
    },
    data(){
      return {
          userResult: '', //사용자 응답 저장하는 데이터
          showPopup: false, //팝업 상태
          dialog: false,
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
        submitSoundRes(){
            if(this.userResult.trim() == ''){
                alert("답변을 입력해주세요!")
            } else {
                if(this.userResult === '꿩'){
                    // 정답 다이얼로그 표시
                    this.dialog = true;
                } else {
                    //오답 다이얼로그 표시
                    this.dialog = true;
                }
            }
        },
        handleDialogConfirmation(correct){
            this.dialog = false;
            if(correct){
                if (this.result1 === false){
                    //result1가 false인 경우만 'answerCorrect' 이벤트를 트리거(마커를 정답 이미지로 바꾸기 위하여)
                    this.$emit('answerCorrect');
                }
                this.userResult = ''; // 사용자 응답 리셋
                this.closeP();        // 다이얼로그 닫기
            }
        }

    }
}
</script>

<style scoped>
    img{
        width: 100%;
        border-radius: 8px;
    }
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
        border-radius: 8px;
        position: fixed; 
        background-color: white;
        overflow:hidden;

        display:flex;
        flex-direction: column; /*수직 배치*/
        align-items: flex-end; /* 오른쪽 정렬 */
      }

      .content-container{
        width:100%;
        position: relative;
        top:10%;
      }

    .close{
        width: 20px;
        height: 20px;

        background-color: #ccc;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;

        justify-content: center;
        align-items: center;
        position:absolute;
        top:10px;
        right:10px;
    
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
      position: absolute; /* 고정 위치 */
      left: 0; /* 왼쪽에 위치 */
      width: 100%; /* 너비를 전체로 설정 */
      background-color: #fff; /* 배경 색상 */
      padding: 10px 20px; /* 패딩을 상하에만 적용 */
      display: flex; /* 버튼들을 가로로 정렬 */
      justify-content: center; /* 가운데 정렬 */
      z-index: 10; /* 다른 요소들 위에 나타나도록 z-index 설정 */
    }
</style>