import Vue from 'vue';
import App from './App.vue';
import VueGeolocationApi from 'vue-geolocation-api';
import VueRouter from 'vue-router';
import router from './router';
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false;

Vue.use(VueGeolocationApi);
Vue.use(VueRouter)

new Vue({
    render: h => h(App),
    vuetify,
    router
}).$mount('#app');