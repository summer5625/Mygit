import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const store = new Vuex.Store({

  //store中一共有五大字段：state  mutations  actions  getter  module
  state:{
    count:1
  },

  mutations:{
    //定义方法中默认要有state参数，第二个参数是用户传入的值
    //mutations中的方法只能做同步操作，不能直接commit

    //异步操作
    addCount(state, val){
      state.count += val;
    },

    //同步操作
    asyncHandler(state, val){
      state.count += val;
    }
  },

  actions:{
    //action可以包含任意异步操作
    asyncHandler({commit}, val){
      commit('asyncHandler', val);
    },

    addCount({commit}, val){
       setTimeout(()=>commit('addCount', val), 1000)
    },
  }
});


export default store;
