// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

//element-ui导入
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

//导入css
import '../static/global/global.css'
import '../static/global/gt.js'

//导入axios插件
import * as api from './restful/api.js'
Vue.prototype.$http=api;

//导入vuex插件
import store from '../src/store/index'

//路由的全局守卫，保证登录后刷新页面用户数据不丢失
router.beforeEach((to, from, next)=>{
  
  if (localStorage.getItem('access_token')) {
    let user = {
      access_token: localStorage.getItem('access_token'),
      username: localStorage.getItem('username'),
      avatar: localStorage.getItem('avatar'),
      notice_num: localStorage.getItem('notice_num'),
      shop_cart_num: localStorage.getItem('shop_cart_num'),
    };
    store.dispatch('getUserInfo', user);
  }
  next();
});


//调用插件
Vue.use(ElementUI);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
