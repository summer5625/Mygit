module.exports={
    //entry入口
    //output出口
    entry:{
        main:'./main.js'
    },
    output:{
        filename:'./bundle.js'  //和在命令行打包差不多，会生成一个bundle.js的文件
    },
    //监听打包文件是否变化，变化后会自动重新打包
    watch:true,
    //配置css文件loader的加载器，要处理不同的文件就要下载配置对应文件的加载器loader
    module:{
        loaders:[
            {
                test:/\.css$/, //必须是test
                loader:'style-loader!css-loader' //表示先识别css-loader再识别style-loade
            }
        ]
    }
};