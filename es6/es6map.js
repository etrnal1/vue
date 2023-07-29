// map 的顺序是被添加到Map中的顺序
var myMap =new Map();
var keyString ="键apple"
myMap.set(keyString,"值macPro")
console.log("得到键: ",myMap.get(keyString))
for(let [key,value] of myMap) {
    console.log(key,value)
}

myMap.forEach((value,key)=>{
    console.log("foreach用法",key)
})
// 判断键是否存在
myMap.has("键apple")
console.log(myMap.size)

// map 键可以是任何类型,包括函数,对象,原始值
// 在频繁增删键值对的场景下,map通常会有更好的性能够
// map 与array相互转换
var kvArray =[["key1","value1"]]
var myMap =new Map(kvArray)

// 将map 对象转换成数组
var outArray = Array.from(myMap);
    console.log("转换过后的数据",outArray)


