import Vue from 'vue'
import VueRouter from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import StartView from '../views/StartView.vue';
// import MainView from '../views/MainView.vue';

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'Remember',
        component: StartView
    },
    {
        path: '/map',
        name: 'MainView',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/MainView.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router