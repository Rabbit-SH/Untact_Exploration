import Vue from 'vue'
import Vuex from 'vuex'
// import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        photos: [],
    },
    getters: {},
    mutations: {
        addPhoto: (state, photoUrl) => {
            state.photos.push(photoUrl);
        }
    },
    actions: {},
    modules: {},
    // plugins: [createPersistedState({
    //     key: 'photos', // 로컬 스토리지에 저장될 데이터의 키
    //     paths: ['photos'], // 저장할 데이터의 경로
    //     // storage: window.sessionStorage, // 세션 스토리지 사용
    // })]
})