
<!--

app.vue文件编写结构：
    1.页面结构（组件结构）template
    2.页面逻辑（组件逻辑）script
    3.页面样式（组件样式）style

    注：相当于一个HTML文件，利用vue-template插件进行解析

-->

<template>

    <!--一定是一个闭合的标签-->
    <div>
        <h3>{{msg}}</h3>
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
        </ul>
        <Header />
    </div>

</template>

<script>
import Header from './Header.vue'

    export default{
        data(){
            return{
                msg:'学习单页面应用'
            }
        },
        methods:{
        },
        computed:{
        },
        components:{
            Header
        }

    }

</script>

<!--添加了scoped表示，样式只对当前的组件样式起作用-->
<style scoped>

//全局的样式
    h3{
        color: white;
     }
</style>

