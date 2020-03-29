<template>
  <div>
    <p>{{myCount}}</p>
  </div>
</template>


<script>
export default {
  name: 'Child',
  data () {
    return {

    }
  },
  //监听数据的变化
  computed:{
    myCount(){
      return this.$store.state.count;
    }
  }
}
</script>


<style scoped>
</style>
