import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home/Home'
import Course from '@/components/Course/Course'
import LightCourse from '@/components/LightCourse/LightCourse'
import Micro from '@/components/Micro/Micro'
import CourseDetail from '@/components/Course/CourseDetail'
import Login from '@/components/Login/Login'
import Cart from  '@/components/Cart/Cart'


//Router当做局部模块使用一定要Vue.use(Router)
//以后在组件中可以通过this.$router获取Router实例化对象
//通过this.$routes获取路由信息对象
Vue.use(Router);

export default new Router({
  linkActiveClass:'is-active',
  mode:'history', //改为history模式后，路由就不会出现很丑的hash
  routes: [
    {//一个路由信息对象
      path: '/',
      redirect:'/home'
    },
    {
      path: '/home',
      name:'Home',
      component: Home
    },
    {
      path: '/course',
      name:'Course',
      component: Course
    },
    {
      path: '/home/light-course',
      name:'LightCourse',
      component: LightCourse
    },
    {
      path: '/micro',
      name:'Micro',
      component: Micro
    },
    {
      path:'/course/detail/web/:detailId',
      name:'CourseDetail',
      component:CourseDetail
    },
    {
      path:'/login',
      name:'Login',
      component:Login
    },
    //购物车页面
    {
      path:'/purchase/shopping_cart',
      name:'purchase.shop',
      component:Cart
    },
  ]
});
