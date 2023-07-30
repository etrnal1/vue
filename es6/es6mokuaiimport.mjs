// import  只读属性,不允许在加载模块的脚本里面,改写接口的引用指向,既可以改写import 变量类型为对象的属性值,不能改写import变量类型为基本类型的值
import {myName,myAge,myfn,myClass} from "./es6mokuaiexport.mjs";
import {t} from "./es6mokuaiexport.mjs"
console.log(myAge)  
console.log(t)