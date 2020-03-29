//整个项目的入口启动文件

//导入npm下载的模块
import Vue from 'vue'

//导入自己编写的模块
import App from './App.vue'

//两个导入不同点在于npm下载的模块：from ‘模块名称’，导入自己编写的模块：from ‘编写模块的路径’

//导入全局组件
import Header from './components/Common/Header.vue'
//注册全局组件
Vue.component(Header.name, Header);

new Vue({
  el: '#app',

  //DOM直接渲染
  render: h => h(App)
});
