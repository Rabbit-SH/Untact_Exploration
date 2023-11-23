import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        photoAlbum: [],
    },
    mutations: {
        addPhoto(state, photoUrl) {
            state.photoAlbum.push(photoUrl);
        },
    },
});