<!-- <template>
  <div>
    <p>시작해볼까</p>
    <button @click="$router.push({name: 'MainView'})">MainView로 이동</button>
  </div>
</template> -->
<template>
  <div>
    <h1> 코스 선택 </h1>
    <br>
    <v-btn> 금강초롱꽃을 찾아줘! </v-btn>
    <br>
    <br>
    <v-btn @click="$router.push({name: 'TutorialPage'})">물두꺼비를 따라가보자! </v-btn>
    <br>
    <br>
    <p> 대상 : 어린아이 </p>
    <p> 체험예상시간: 1시간 30분 </p>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>