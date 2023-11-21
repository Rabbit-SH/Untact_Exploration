import Vue from 'vue'
import VueRouter from 'vue-router'
import StartView from '../views/StartView.vue';
import MainView from '../views/MainView.vue';
import TutorialPage from '../views/TutorialPage.vue';
import AIView from '../components/NaviView/AIView.vue';
import FinalView from '../components/FinalView.vue';

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: StartView, name: 'StartView' },
        { path: '/map', component: MainView, name: 'MainView' },
        { path: '/tutorial', component: TutorialPage, name: 'TutorialPage' },
        { path: '/ai', component: AIView, name: 'AIView' },
        { path: '/final', component: FinalView, name: 'FinalView' },
    ]
})

export default router