<template>
  <div id="app">
    <LuffyHeader></LuffyHeader>
    <router-view></router-view>
  </div>
</template>

<script>
import LuffyHeader from '@/components/common/LuffyHeader'

export default {
  name: 'App',
  components:{
    LuffyHeader
  }
}
</script>

<style scoped>

</style>
