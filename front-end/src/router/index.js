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
        { path: '/waterfrog/map', component: MainView, name: 'MainView' },
        { path: '/waterfrog/tutorial', component: TutorialPage, name: 'TutorialPage' },
        { path: '/waterfrog/ai', component: AIView, name: 'AIView' },
        { path: '/waterfrog/final', component: FinalView, name: 'FinalView' },
    ]
})

export default router