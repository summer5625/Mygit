//axios请求处理
//导入axios插件
import Axios from 'axios'
Axios.defaults.baseURL = 'https://www.luffycity.com/api/v1/';



// 添加请求拦截器
Axios.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么,将用户信息添加到请求头，用于用户购买或者加入购物车的身份认证
  if (localStorage.getItem('access_token')){
    // Axios.defaults.headers.common['Authorization'] = localStorage.getItem('access_token');
    console.log(config.headers);
    config.headers.Authorization = localStorage.getItem('access_token');
  }
  return config;
  }, function (error) {
    // 对请求错误做些什么
  return Promise.reject(error);
  });

//获取分类列表
export const categoryList = ()=>{
  return Axios.get('course_sub/category/list/').then(res=>res.data);
};

//获取所有的课程列表
export const allCategoryList = (categoryId)=>{
  return Axios.get(`courses/?sub_category=${categoryId}`).then(res=>res.data);
};

//课程详情顶部数据
export const courseDetailTop = (courseId)=>{
  return Axios.get(`course/${courseId}/top/`).then(res=>res.data)
};

//课程概述
export const coursedetail = (courseid)=>{
  return Axios.get(`course/${courseid}/detail/`).then(res=>res.data)
};

//geetest接口登录滑动验证
export const geetest = ()=>{
  return Axios.get(`captcha_check/`).then(res=>res.data)
};

//登录
export const userLogin = (params)=>{
  //参数有5个字段：username password和验证的三个字段
  return Axios.post('account/login/', params).then(res=>res.data);
};

// 加入购物车的接口
export const shopCart = (params)=>{
	return Axios.post('user/shop_cart/create/',params).then(res=>res.data);
};

// 购物车的数据
export const shopCartList = ()=>{
	return Axios.get(`user/shop_cart/list/`).then(res=>res.data);
};
