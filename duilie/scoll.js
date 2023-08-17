在 JavaScript 中，可以使用 `window.scrollTo` 方法来滚动到页面底部。以下是一个例子：

```javascript
window.scrollTo(0, document.body.scrollHeight);
```

在这个例子中，`window.scrollTo` 方法接受两个参数：第一个参数是要滚动到的 x 坐标，第二个参数是要滚动到的 y 坐标。`document.body.scrollHeight` 是整个页面的总高度，所以这行代码的效果就是滚动到页面底部。

如果你想在滚动到底部后执行某些操作，可以使用 `window.setTimeout` 方法来添加一个延时：

```javascript
window.scrollTo(0, document.body.scrollHeight);
window.setTimeout(function() {
    // 在这里添加你的代码...
}, 2000);  // 2秒后执行
```

在这个例子中，我们在滚动到底部后等待了 2 秒，然后执行了 `function` 中的代码。这个等待时间是为了确保页面有足够的时间加载。这个等待时间可能需要根据实际情况进行调整。



在很多情况下，例如在加载无限滚动的网页时，仅仅滚动到页面底部并不能加载所有内容，因为每次滚动到底部时，网页可能会自动加载更多的内容。在这种情况下，你需要反复滚动到底部，直到没有更多的内容被加载。

以下是一个使用 JavaScript 实现这个功能的基本方法：

```javascript
function scrollToBottom() {
    // 滚动到底部
    window.scrollTo(0, document.body.scrollHeight);

    // 检查页面高度是否发生变化
    var currentHeight = document.body.scrollHeight;
    setTimeout(function() {
        if (currentHeight < document.body.scrollHeight) {
            // 如果页面高度增加，继续滚动
            scrollToBottom();
        } else {
            // 否则，已经滚动到了最底部
            console.log("Reached bottom");
        }
    }, 1000);  // 等待1秒后再检查
}

// 调用函数开始滚动
scrollToBottom();
```

