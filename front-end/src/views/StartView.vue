<template>
  <div>
    <v-img :src="require('@/assets/tutorialView/표지 예시.png')"
    @click="$router.push({name:'CourseChoose'})"></v-img>
    <div justify="center" align="center" class="text-container">
      <p> 화면을 클릭해주세요 ! </p>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.text-container {
  position: absolute;
  top: 10%; /* 세로 가운데 정렬을 위해 50%로 설정 */
  left: 50%; /* 가로 가운데 정렬을 위해 50%로 설정 */
  transform: translate(-50%, -50%); /* 정확한 중앙 정렬을 위한 transform */
  text-align: center; /* 가운데 정렬을 위해 텍스트를 가운데 정렬 */
  color: gray; /* 글씨 색상을 회색으로 설정 */
}
</style>