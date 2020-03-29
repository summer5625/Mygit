module.exports={
    //entry入口
    //output出口
    entry:{
        main:'./src/main.js'
    },
    output:{
        filename:'./bundle.js'  //和在命令行打包差不多，会生成一个bundle.js的文件
    },
    //监听打包文件是否变化，变化后会自动重新打包
    watch:true
};