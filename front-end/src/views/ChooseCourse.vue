<template>
  <div>
    <v-img :src="require('@/assets/tutorialView/코스 선택.png')" class="course_img">
      <div class="A"></div>
      <v-btn class="B" @click="$router.push({name: 'TutorialPage'})"></v-btn>
    </v-img>

    
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
.course_img {
  position: relative;
}
.A,
.B {
  position: absolute;
  bottom: 7%;
  left: 57%;
  width: 36%;
  height: 19%;

}
@media (max-width: 600px) {
  .B {
    bottom: 7%;
    left: 57%;
    width: 36%;
    height: 19%;
  }
}
.theme--light.v-btn.v-btn--has-bg {
    background-color: transparent;
}
.v-btn:not(.v-btn--round).v-size--default {
    height: 19%;
    min-width: 64px;
}
.v-btn--is-elevated {
    box-shadow: none;
}
</style>