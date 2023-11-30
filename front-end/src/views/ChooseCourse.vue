<template>
  <div>
    <v-img :src="require('@/assets/tutorialView/코스 선택.png')" class="course_img"></v-img>
    <div class="A"></div>
    <div class="B" @click="$router.push({name: 'TutorialPage'})"></div>
  </div>
</template>

<script>
export default {
}
</script>

<style>
.course_img {
  position: relative;
}
.A,
.B {
  position: absolute;

  width: 30%; /* 이미지에 따라 조절하세요 */
  height: 30%;
  /* background-color: white; */
  background-color: transparent; /*배경을 투명하게 만듭니다*/
  cursor: pointer; /* 마우스를 올렸을 때 포인터로 변경됩니다 */
}
.A {
  top: 18%;
  left: 30%;
}
.B {
  bottom: 7%;
  left: 57%;
  width: 36%;
  height: 19%;
}
</style>