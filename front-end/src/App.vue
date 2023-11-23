<template>
  <v-app>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
  methods: {
  // localStorage의 모든 데이터를 삭제하는 메소드
    clearLocalStorage() {
      localStorage.clear();
    }
  },
  created() {
    // beforeunload 이벤트 리스너를 추가합니다
    window.addEventListener('beforeunload', this.clearLocalStorage);
  },
  beforeDestroy() {
    window.removeEventListener('beforeunload', this.clearLocalStorage);
  }
};
</script>
