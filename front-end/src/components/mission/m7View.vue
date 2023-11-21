<template>
    <div class="black-bg" v-if="show">
        <div class="white-bg">
            <img :src="require('@/assets/mission/bg-7.png')">

            <button class="close" @click="closeP">X</button>
            <div class="content-container" justify="center" align="center">
                <v-textarea
                    class="mx-2"
                    label="소원을 적어주세요 !"
                    v-model="userResult"
                    style="width: 80%;"
                    prepend-icon="mdi mdi-hands-pray"
                ></v-textarea>
                
                
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
                                <v-img src="@/assets/O.png" style="max-height:100%; max-width:100%;"></v-img>
                            </div>
                            <br>
                            <div class="text-center">
                                <h3>꼭 소원이 이루어질거에요 !</h3> 
                                <br>
                                <h4>다음 미션으로 가볼까요?</h4>
                                <h5><strong>확인</strong> 버튼을 눌러주세요.</h5>
                            </div>
                        </v-col>
                    </v-row>
                </v-card-text>
                <v-card-actions>
                <v-btn @click="handleDialogConfirmation(userResult)" class="ml-auto">확인</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script >
export default {
    props: {
        show: {
            type: Boolean,
            required: true,
        },
        result7: {
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
        submitSoundRes(){
            if(this.userResult.trim() == ''){
                alert("답변을 입력해주세요!")
            } else {
                this.dialog = true;
            }
        },
        handleDialogConfirmation(correct){
            this.dialog = false;
            if(correct){
                if (this.result7 === false){
                    //result7가 false인 경우만 'answerCorrect' 이벤트를 트리거(마커를 정답 이미지로 바꾸기 위하여)
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
    .textarea{
        justify-content: center;
    }

</style>