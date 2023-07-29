// set 对象
var mySet = new Set([1,2,3,4,4])
console.log("set 数组去重   ",mySet)

// 数组去重

//数组并集 [两个数据的差集]
var a=new Set([1,2,3]);
var b=new Set([4,3,2])
console.log(new Set(a,b))

//数组交集
// 这些代码片段使用了JavaScript的 `Set` 对象和数组方法来找出两个集合的交集。

// 首先，让我们分步骤地解释这些代码：

// 1. **创建 Set**：`Set` 是一种特殊类型的对象，其中每个元素都是唯一的。`new Set([1, 2, 3])` 和 `new Set([4, 3, 2])` 创建了两个新的 `Set` 对象，分别保存了数组 `[1, 2, 3]` 和 `[4, 3, 2]` 的元素。

//    ```javascript
//    var a = new Set([1, 2, 3]); // a 保存 {1, 2, 3}
//    var b = new Set([4, 3, 2]); // b 保存 {4, 3, 2}
//    ```

// 2. **使用 Spread Operator**：`...` 是 JavaScript 的扩展运算符，可以将一个集合（如数组或 `Set`）的所有元素拆开。`[...a]` 创建了一个新的数组，包含了 `Set` `a` 的所有元素，即 `[1, 2, 3]`。

// 3. **数组的 `filter` 方法**：`filter` 是数组的一种方法，它接收一个函数作为参数，这个函数应用于数组的每个元素。只有当函数返回 `true` 时，该元素才会出现在返回的新数组中。在这里，`filter` 方法接收的函数是 `x => b.has(x)`，这是一个箭头函数，它检查 `Set` `b` 是否包含元素 `x`。

//    ```javascript
//    [...a].filter(x => b.has(x)) // 返回 [2, 3]
//    ```

// 4. **创建交集 Set**：最后，`new Set([...a].filter(x => b.has(x))` 创建了一个新的 `Set`，包含了上一步骤返回的数组的所有元素。因此，`intersect` 是两个 `Set` `a` 和 `b` 的交集：

//    ```javascript
//    var intersect = new Set([...a].filter(x => b.has(x))); // intersect 保存 {2, 3}
//    ```

// 所以，这段代码实现了找出两个集合（`Set`）的交集的功能。希望这个解释对你有所帮助！
var a=new Set([1,2,3]);
var b=new Set([4,3,2])
//`...` 是 JavaScript 的扩展运算符，可以将一个集合（如数组或 `Set`）的所有元素拆开。`[...a]` 创建了一个新的数组，包含了 `Set` `a` 的所有元素，即 `[1, 2, 3]`。

var d =new Set([...a].filter(x=> !b.has(x)))
console.log(d)


//数组差集