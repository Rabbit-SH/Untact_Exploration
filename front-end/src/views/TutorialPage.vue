<template>
  <v-carousel hide-delimiters height="auto" 
  :cycle="false"
  :continuous="false"
  @input="handleSliderChange">
    <v-carousel-item v-for="(item, i) in items" 
    :key="i" 
    :src="item.src">
    <v-btn 
    v-show="i === 1"
    @click="startsound"
    :color="buttonPressed ? 'blue' : 'defaultColor'"
    fab
    small
    style="top: 1%; left: 1%;"
    >
      <v-icon>mdi mdi-volume-high</v-icon>
    </v-btn>
      <v-btn x-small color="teal" dark 
      @click="goToMain" class="skipButton">Skip</v-btn>
      <v-btn x-small color="primary" dark
      class="beforeButton"
      v-if="i==0" @click="$router.push({name:'CourseChoose'})">이전으로</v-btn>
    </v-carousel-item>
    <!-- 마지막 페이지에만 컨트롤 버튼을 표시X -->
    <v-carousel-item v-if="!hasNext" :src="require('@/assets/tutorialView/게임시작 페이지 예시.png')">
      <div class="goToMainPage" @click="goToMain"></div>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { src: require('@/assets/tutorialView/캐릭터 소개 예시.png')},
        { src: require('@/assets/tutorialView/튜토리얼1.png'),audio: require('@/assets/test1.mp3') },
        { src: require('@/assets/tutorialView/튜토리얼2.jpg')},
        { src: require('@/assets/tutorialView/튜토리얼3.png')},
      ],
      currentAudio: null, // 현재 재생 중인 오디오
      started: false,
      buttonPressed: false,

    };
  },
  computed: {
    // 현재 페이지가 마지막 페이지인지 확인
    hasNext() {
      return this.$refs.carousel ? this.$refs.carousel.hasNext() : false;
    },
  },
  methods:{
    playAudio(audioSrc) {
      if (this.currentAudio) {
        this.currentAudio.pause(); // 이전 오디오 정지
      }
      this.currentAudio = new Audio(audioSrc);
      this.currentAudio.play();
    },
    goToMain() {
      if (this.currentAudio) {
        this.currentAudio.pause(); // 오디오 정지
      }
      this.$router.push({ name: 'MainView' });
    },
    startsound() {
    this.playAudio(this.items[1].audio);
    this.buttonPressed = true;
    },
    handleSliderChange(index){
      //인덱스가 유효한지 확인
      if(index !== undefined && index >= 0){
        this.playAudio(this.items[index].audio);
      }
    }
  }
};
</script>

<style scoped>
.beforeButton{
position: absolute;
top:10px;
left: 10px;
}
.skipButton {
position: absolute;
top: 10px;
right: 10px;
}
.goToMainPage {
position: absolute;
bottom: 15%;
left: 10%;
width: 80%;
height: 10%;
}
</style>