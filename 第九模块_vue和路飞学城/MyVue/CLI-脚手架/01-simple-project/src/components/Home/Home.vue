<template>
  <div class="home">
    首页===={{text}}
    <button @click="addHandler">触发</button>
  </div>
</template>


<script>

  export default {
    name:'home',
    methods:{
      addHandler(){
        this.$emit('add', '嘿嘿嘿')
      }
    },
    data(){
      return{

      }
    },
    props:['text']
  }

</script>


<style lang="css" scoped></style>
