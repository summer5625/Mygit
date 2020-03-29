import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

let store = new Vuex.Store({

  state:{
    userInfo:{},
  },

  mutations:{
    getUserInfo(state, user){
      state.userInfo = user;
    }
  },

  actions:{
    getUserInfo({commit}, user){
      commit('getUserInfo', user);
    }
  }

});

export default store;
