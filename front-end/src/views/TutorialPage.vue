<template>
    <v-carousel hide-delimiters height="auto" 
    :cycle="false"
    :continuous="false">
      <v-carousel-item v-for="(item, i) in items" 
      :key="i" 
      :src="item.src">
        <v-btn x-small color="teal" dark 
        @click="goToMain" class="skipButton">Skip</v-btn>
        <v-btn x-small color="primary" dark
        class="beforeButton"
        v-if="i==0" @click="$router.push({name:'CourseChoose'})">이전으로</v-btn>
      </v-carousel-item>
      <!-- 마지막 페이지에만 컨트롤 버튼을 표시X -->
      <v-carousel-item v-if="!hasNext" :src="require('@/assets/tutorialView/last_tu.png')">
        <img 
        :src="require('@/assets/start_button_img.png')"
        @click="goToMain" class="moveToMainButton" />
      </v-carousel-item>
    </v-carousel>
</template>
  
<script>
  export default {
    data() {
      return {
        items: [
          { src: require('@/assets/tutorialView/캐릭터 소개 예시.png') },
          { src: require('@/assets/tutorialView/튜토리얼_병합.jpg') },
          { src: require('@/assets/tutorialView/튜토리얼_마지막.png') },
          // { src: require('@/assets/tutorialView/tutorial2.png') },
          // { src: require('@/assets/tutorialView/tutorial3.png') },
        ],
      };
    },
    computed: {
      // 현재 페이지가 마지막 페이지인지 확인
      hasNext() {
        return this.$refs.carousel ? this.$refs.carousel.hasNext() : false;
      },
    },
    methods:{
        goToMain(){
            this.$router.push({ name: 'MainView' });
        }
    }
  };
</script>

<style scoped>
.moveToMainButton {
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
}
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
</style>