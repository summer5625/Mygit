<template>
  <div>
    <h3>{{myCount}}</h3>
    <Child></Child>
    <button @click="changeCount">异步修改</button>
    <button @click="asyncHandler">同步修改</button>
  </div>

</template>


<script>
  import Child from './child'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },

  methods:{
    changeCount(){
      //修改vuex的store中的状态state的唯一方法就是提交mutations
      //第一个参数是数据仓库store的mutations中定义的方法名称

      //触发mutations中的方法用commit，触发action中的方法用dispatch
      // this.$store.commit('addCount', 3);
      this.$store.dispatch('addCount', 3);
    },

    asyncHandler(){
      // this.$store.commit('asyncHandler', 2);
      this.$store.dispatch('asyncHandler', 2);
    }
  },

  //监听数据的变化
  computed:{
    myCount(){
      return this.$store.state.count;
    }
  },
  components:{
    Child
  }
}
</script>


<style scoped>
</style>
