import Vue from 'vue'
import VueRouter from 'vue-router'
import MainView from '../views/MainView.vue';
import TutorialPage from '../views/TutorialPage.vue';
import AIView from '../components/NaviView/AIView.vue';
import FinalView from '../components/FinalView.vue';

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/watertoad/map', component: MainView, name: 'MainView' },
        { path: '/watertoad/', component: TutorialPage, name: 'TutorialPage' },
        { path: '/watertoad/ai', component: AIView, name: 'AIView' },
        { path: '/watertoad/final', component: FinalView, name: 'FinalView' },
    ]
})

export default router