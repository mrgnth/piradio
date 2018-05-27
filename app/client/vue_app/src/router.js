import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Api from './views/Api.vue'
import Manage from './views/Manage.vue'
import Radio from './views/Radio.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    },
    {
      path: '/manage',
      name: 'manage',
      component: Manage
    },
    {
      path: '/radio',
      name: 'radio',
      component: Radio
    }
  ]
})
