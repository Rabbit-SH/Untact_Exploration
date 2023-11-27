import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import './fonts/fonts.css';

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    vuetify,
    render: h => h(App),
    mounted() {
        // 애플리케이션이 마운트될 때 라우터를 사용하여 리디렉션합니다.
        this.$router.push('/waterfrog/tutorial');
    },
}).$mount('#app');