// import name from './app.vue'
//
// console.log(name);
//
// import {age, fav, add} from './app.vue'
//
// console.log(age);
// console.log(fav);
// add();
//
//导入所有的对象
import App from './app.vue'

console.log(App.default);

import Vue from './vue.js'

//导入css文件
import './main.css'

new Vue({
    el:'#app',
    data(){
        return{

        }
    },
    template:`<App />`,
    components:{
        App
    }
});





