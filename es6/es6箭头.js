//this 的绑定方式不同
//没有argumnets对象,箭头函数不能绑定argumentS对象
// 不能使用new 关键字

// 没有prototype属性

// 不能使用yield 关键字
// 简洁的语法
let hello = ()=>{
    console.log("hello ")
}
hello();
let square=x=>{
    return x*x 
}

console.log("箭头函数初始参数",square(5))
// 使用箭头函数还是普通函数取决于场景
function ArrowFunction(){
    this.value=1;
    setTimeout(()=>{
        console.log(this.value)
    },100)
}

ArrowFunction()
