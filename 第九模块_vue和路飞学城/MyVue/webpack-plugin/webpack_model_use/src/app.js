//es6的model
//export抛出变量，值等对象

let name='alex';

export default name;

let age='23';
export {age}

export var fav='电竞毒奶';

export function add() {
    console.log('抛出了函数啊!')
}

let App = {
    template:`<div>我是一个粉刷匠</div>`
};

export {App}