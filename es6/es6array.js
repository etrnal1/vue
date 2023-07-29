console.log("创建数组",Array.of(1,2,3,4))


console.log(Array.of(1,2,'3',true)) 


console.log(Array.of())

// 将类数组对象或可迭代对象转换为数组

console.log("将数组对象或可迭代对象转化为数组",Array.from([1,2]))

// 参数为空位
console.log(Array.from([1,,3]))

// this.arg 
let map ={
    do:function(n){
        return n*2
    }
}
let arrayLike = [1,3,4]
console.log(Array.from(arrayLike,function(n){
    return this.do(n)
},map))

// array find      

let arr=[1,2,3,4]
console.log("find查找相关数据[符合条件的多个数据,只返回第一个数据]",arr.find(item=>item>1))

// 查找索引  
let arrs= [7,8,11,12]
console.log("查找索引: ",arrs.findIndex(item=>item == 12))

// 遍历键明

for(let key of['a','b'].keys()){
        console.log(key)
}



for(let value of['a','b'].values()){
    console.log(value)
}