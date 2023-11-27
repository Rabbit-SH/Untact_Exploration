import Vue from 'vue'
import VueRouter from 'vue-router'
import StartView from '../views/StartView.vue';
import MainView from '../views/MainView.vue';
import TutorialPage from '../views/TutorialPage.vue';
import AIView from '../components/NaviView/AIView.vue';
import FinalView from '../components/FinalView.vue';
import CourseChoose from '../views/CourseChoose.vue';

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        { path: '/waterfrog/', component: StartView, name: 'StartView' },
        { path: '/waterfrog/map', component: MainView, name: 'MainView' },
        { path: '/waterfrog/tutorial', component: TutorialPage, name: 'TutorialPage' },
        { path: '/waterfrog/ai', component: AIView, name: 'AIView' },
        { path: '/waterfrog/final', component: FinalView, name: 'FinalView' },
        { path: '/waterfrog/cousrse', component: CourseChoose, name: 'CourseChoose' },
    ]
})

export default router