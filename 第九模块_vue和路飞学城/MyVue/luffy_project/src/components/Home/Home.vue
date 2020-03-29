<template>

  <!--轮播图-->
<!--  <el-carousel indicator-position="outside" height="400px">-->
<!--    <el-carousel-item v-for="item in lunboImgs" :key="item.id">-->
<!--      <img :src="item.imgSrc" alt="">-->
<!--    </el-carousel-item>-->
<!--  </el-carousel>-->

  <el-carousel :interval="5000" arrow="always">
    <el-carousel-item v-for="item in lunboImgs" :key="item.id">
      <img :src="item.imgSrc" alt="">
    </el-carousel-item>
  </el-carousel>

</template>


<script>

  export default {
    name:'Home',

    data(){
      return{
        lunboImgs:[
          {
            id:1,
            imgSrc:'//hcdn1.luffycity.com/static/frontend/index/banner1_1574421633.826987.png'
          },
          {
            id:2,
            imgSrc:'//hcdn1.luffycity.com/static/frontend/index/banner1_1567492241.7829425.png'
          },
          {
            id:3,
            imgSrc:'//hcdn1.luffycity.com/static/frontend/index/banner2@2x_1567507260.133423.png'
          },
          {
            id:4,
            imgSrc:'//hcdn1.luffycity.com/static/frontend/index/banner3_1567492242.652474.png'
          }
        ]
      }
    },

    created(){
      // console.log(localStorage);
    },
  }

</script>


<style scoped>

  img {
    width: 100%;
  }

</style>


