import { createRouter, createWebHistory } from 'vue-router'
import HomeView from './view/Home.vue'
import SekyuLoginVue from './view/SekyuLogin.vue'
import SekyuPageVue from './view/SekyuPage.vue'
import OSADVue from './view/OSAD.vue'
import OSADLoginVue from './view/OSADLogin.vue'
import SignUpSecurity from './view/SignUpSecurity.vue'
import SignUpOSAD from './view/SignUpOSAD.vue'
import Violations from './components/Violations.vue'
import ForgotPasswordSecurity from './view/ForgotPasswordSecurity.vue'
import ForgotPasswordOSAD from './view/ForgotPasswordOSAD.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/SekyuLogin',
      name: 'SekyuLogin',
      component: SekyuLoginVue
    },
    {
      path: '/SekyuPage',
      name: 'SekyuPage',
      component: SekyuPageVue
    },
    {
      path: '/OSAD',
      name: 'OSAD',
      component: OSADVue
    },
    {
      path: '/OSADLogin',
      name: 'OSADLogin',
      component: OSADLoginVue
    }
    ,
    {
      path: '/SignUpSecurity',
      name: 'SignUpSecurity',
      component: SignUpSecurity
    }
    ,
    {
      path: '/SignUpOSAD',
      name: 'SignUpOSAD',
      component: SignUpOSAD
    },
    {
      path: '/Violations',
      name: 'Violations',
      component: Violations
    },
    {
      path: '/ForgotPasswordSecurity',
      name: 'ForgotPasswordSecurity',
      component: ForgotPasswordSecurity
    },
    {
      path: '/ForgotPasswordOSAD',
      name: 'ForgotPasswordOSAD',
      component: ForgotPasswordOSAD
    },
  ]
})

export default router
