import Vue from 'vue'
import Router from 'vue-router'
import Home from './components/Home.vue'
import Render from './components/Render.vue'
import About from './components/About.vue'
import Nf from './components/Nf.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/render',
      name: 'Render',
      component: Render
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '*',
      name: 'Nf',
      component: Nf
    },
  ]
})
