//let 不存在变量提升 在声明a时,变量提升,但未赋值,所以报undefined

var a="apple"
console.log(a)  

// const 声明一个常量 变量指向的内存地址保存的数据不想允许改动
const PI='3.1415'

console.log(PI)