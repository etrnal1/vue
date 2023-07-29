// es6 解构赋值
// 解构的源头 = 解构的目标 是赋值运算符的扩展
let [a,b,c] =[1,2,3]
console.log(a,b,c)

// 可遍历对象 ,即可复制
let [f,g,h,i,s]= 'hello'
console.log("数据的值:",f)
// 对象模型的解构 (object)

let {foor,bar} ={foor:"bar",bar:"bbb"}

console.log(foor)
console.log(bar)
// 解构表达式,将baz的属性值赋予foo变量
let {baz:foo} ={baz:'ddd'}
console.log(foo)
// 这是一种在JavaScript中用于解构赋值的语法。解构赋值是一种允许我们从数组或对象中提取值，然后将它们分配给变量的表达式。在你提供的代码中，`{baz: foo} = {baz: 'ddd'}`，它是一个对象解构赋值的例子。

// 这段代码的工作原理如下：

// 1. `{baz: 'ddd'}` 是一个对象，其中 `baz` 是属性名，`'ddd'` 是属性值。
// 2. `{baz: foo}` 是一个解构表达式，它将 `baz` 属性的值赋给 `foo` 变量。这里的 `:` 是解构别名语法，表示将 `baz` 的值赋给一个新的变量 `foo`。
// 3. 于是，`foo` 的值就是 `'ddd'`。

// 在这个例子中，`foo` 是从对象中解构出来的新变量，其值就是 `'ddd'`。这是一种非常方便的方式，可以轻松地从对象或数组中提取并使用值。

// 这就是JavaScript中解构赋值的基本用法。希望这个答案对你有所帮助！