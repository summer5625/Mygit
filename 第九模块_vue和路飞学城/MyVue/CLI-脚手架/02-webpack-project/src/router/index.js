//整个路由的配置文件

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home/Home.vue'  //@相当于src文件夹的路径
import FreeCourse from '@/components/FreeCourse/FreeCourse.vue'

//让vue使用vue-router插件
Vue.use(VueRouter);

//挂载插件
var router = new VueRouter({
  routes:[
    {
      path:'/',
      name:'home',
      component:Home
    },
    {
      path:'/free',
      name:'freeCourse',
      component:FreeCourse
    }
  ]
});

export default router
