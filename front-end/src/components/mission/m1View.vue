<template>
    <div class="black-bg" v-if="show">
        <div class="white-bg">
            <button class="close" @click="closeP">
                <img src="@/assets/mission/close.png">
            </button>
            <div class="content-container" justify="center" align="center">
                <v-row class="sound-item pl-7 pr-7">
                    <v-col cols="4">
                        <v-btn @click="toggleAudio(sounds[0])" fab>
                            <v-icon large  :style="{ color: sounds[0].isActive ? 'green' : 'gray' }">mdi mdi-volume-high</v-icon>
                        </v-btn>
                    </v-col>
                    <v-col cols="4">
                        <v-btn @click="toggleAudio(sounds[1])" fab>
                            <v-icon large  :style="{ color: sounds[1].isActive ? 'green' : 'gray' }">mdi mdi-volume-high</v-icon>
                        </v-btn>
                    </v-col>
                    <v-col cols="4">
                        <v-btn @click="toggleAudio(sounds[2])" fab>
                            <v-icon large  :style="{ color: sounds[2].isActive ? 'green' : 'gray' }">mdi mdi-volume-high</v-icon>
                        </v-btn>
                    </v-col>
                </v-row>
                <v-row class="sound-item pr-3 pl-3" justify="center">
                    <v-col cols="auto" class="ma-7">
                        <v-checkbox v-model="userResult" :value="sounds[0].value"></v-checkbox>
                    </v-col>
                    <v-col cols="auto" class="ma-7">
                        <v-checkbox v-model="userResult" :value="sounds[1].value"></v-checkbox>
                    </v-col>
                    <v-col cols="auto" class="ma-7">
                        <v-checkbox v-model="userResult" :value="sounds[2].value"></v-checkbox>
                    </v-col>
                </v-row>
                <br>
                <v-btn class="custom-submit-button mt-3 pl-10 pr-10" color="#EF8200" @click="submitSoundRes">제출하기</v-btn>
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
                                <br>
                                <br>
                                <h4> 이제 진짜 미션을 시작하러 가볼까요? </h4>
                                <br>
                                <h4> 아래의 버튼을 누르면 </h4>
                                <h4> 시작 위치를 알려줄거에요! </h4>
                                <br>
                                <p>버튼을 눌러주세요.</p>
                            </div>
                            <div v-else class="text-center">
                                <h3>다시 한번 풀어볼까요?</h3>
                            </div>
                        </v-col>
                    </v-row>
                </v-card-text>
                <v-card-actions class="card">
                <v-btn @click="handleDialogConfirmation(userResult === '꿩')" class="ok-btn mt-3 pl-10 pr-10" color="#EF8200">{{ userResult === '꿩' ? '찐 미션 고고씽' : '확인' }}</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script scoped>
import { Howl } from 'howler';

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

            sounds: [
                { id: 1, src: "/꿩.wav", isActive: false, howl: null, value: '꿩' },
                { id: 2, src: "/99941F4C5CF91EAC0F.mp3", isActive: false, howl: null, value: '참새' },
                { id: 3, src: "/비둘기.wav", isActive: false, howl: null, value: '비둘기' },
            ],
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
            this.stopAllSounds();
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
        stopAllSounds() {
            this.sounds.forEach((sound) => {
                if (sound.playing) {
                    sound.howl.stop();
                    sound.playing = false;
                    sound.isActive = false;
                }
            });
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
        },
        toggleAudio(sound) {
            this.stopAllSoundsExcept(sound.id);

            if (sound.playing) {
                sound.howl.stop();
            } else {
                sound.howl = new Howl({
                src: [sound.src],
                volume: 1,
                onend: () => {
                    sound.playing = false;
                },
                });
                sound.howl.play();
                sound.playing = true;
            }

            // 토글하여 초록색 스타일 변경
            sound.isActive = !sound.isActive;
        },
        stopAllSoundsExcept(exceptId) {
            this.sounds.forEach((sound) => {
                if (sound.playing && sound.id !== exceptId) {
                sound.howl.stop();
                sound.playing = false;
                sound.isActive = false; // 다른 사운드 중지 시에는 isActive를 false로 설정
                }
            });
        },

    }
}
</script>

<style scoped>
    img{
        width: 100%;
        border-radius: 8px;
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
        position: fixed; 
        /* background-color: white; */
        overflow:hidden;
        display:flex;
        flex-direction: column; 
        align-items: flex-end;
        background-image: url('@/assets/mission/bg_1.png');
        background-size: contain; /* 배경 이미지 크기 조정 옵션 */
        background-position: center; /* 배경 이미지 위치 조정 옵션 */
        background-repeat: no-repeat; /* 배경 이미지 반복 설정 */
      }
    .content-container{
        width:100%;
        position: absolute;
        bottom: 7%;
    }
    .close{
        width: 22px;
        height: 22px;
        cursor: pointer;
        justify-content: center;
        align-items: center;
        position:absolute;
        top: 3%;
        right: 5%;
    
    }
    .custom-submit-button {
        color: white !important; /* 텍스트 색상을 흰색으로 */
        font-weight: bold; /* 글씨 두께를 굵게 */
        font-size: 18px; /* 글씨 크기를 18px로 설정 */
    }
    .card {
    justify-content: center; /* 내부 요소를 중앙 정렬 */
    }
    .ok-btn{
        color: white !important; 
        font-weight: bold; 
        font-size: 18px;
    }
    .center-checkbox {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>