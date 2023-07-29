// 声明函数
function fn(name,age=17){
    console.log(name+",",+age)
}

// 不定参数

function f(...values){

    console.log(values.length)

}
f(1,2)
f(1,2,3,4)

// 箭头函数
console.log("箭头函数..............")
// 参数=>函数体

var f=v=>v 
// var f= function(a){
//     return a;
// }
console.log(f(10))

console.log("箭头函数两个值")
var fs=(a,b)=>a+b  //一行只有结果返回{}
console.log(fs(7,8))

//当箭头函数整体有多行语句,用{}包裹起来,
var fs=(a,v)=>{
    let result =a+b;
    return result  
}

console.log("箭头函数返回对象")
var fo = (id,name)=>({id:id,name:name})
console.log(fo(6,2))

// es6直接使用this 
console.log("维护一个this上下文的时候")
var Person = {
    'age':18,
     'sayHello':function(){
        setTimeout(()=>{
            console.log(this.age)
        });
     }
}

var age=20;
console.log(Person.sayHello());

