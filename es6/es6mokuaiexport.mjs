//export import 
// 基本语法,模块导入导出各种类型的变量,如字符串,数值,函数,类
// export 命令可以出现在模块的任何位置
// import 命令会提升到整个模块的头部m
let tom='cs'

let myName = 'Tom'
let myAge=20;
let myfn=function(){
    return "my name is"
}
let myClass = class myClass{
    static a ="yeah!";
}
//export 命令导出接口,需和模块内部的变量有一一对应关系
//导入的变量名,徐和导出的接口名称相同,即顺序可以不一致
export {myName,myAge,myfn,myClass}
export {tom as t}

