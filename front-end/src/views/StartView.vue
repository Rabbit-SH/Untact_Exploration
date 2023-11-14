<template>
  <div>
    <p>시작해볼까</p>
    <button @click="$router.push({name: 'MainView'})">MainView로 이동</button>
    <!-- <router-link to="/map">메인 지도 이동</router-link>
    <router-view /> -->
  </div>
</template>

<script>
// import {useRouter} from 'vue-router';

export default {
  // setup(){
  //   const router = useRouter();

  //   const goToMainView = () => {
  //     router.push('/map');
  //   }

  //   return{ goToMainView };
  // },
}
</script>

<style>

</style>