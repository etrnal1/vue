# vue
## vue 常用词汇
component
data
methods 
template 
$emit
increment
v-on  简写 @
v-bind 简写:

fillter
`
<router-link to="/foo">Go to Foo</router-link>
        <router-link to="/bar">Go to bar</router-link>
        <router-view></router-view>
`
## vue $emit

在 Vue.js 中，`$emit` 是一个实例方法，用于触发一个自定义事件。这种方法的常见用途是在子组件中触发一个事件，然后父组件可以监听并对这个事件进行响应。

这是一个 `$emit` 的基本用法：
## vue 数据示范

Vue 构造器中有一个el 参数，它是 DOM 元素中的 id
data 用于定义属性，实例中有三个属性分别为：site、url、alexa。
methods 用于定义的函数，可以通过 return 来返回函数值。
{{ }} 用于输出对象属性和函数返回值。

`
var data={site:'测试',url:"www.qian.com",site:"千"}
    var vm=new Vue({
        el:"#app",
        data:{
            message:"hello",
            url:"www.example.com",
            site:"百度"
        },
        methods:{
            details:function(){
                return this.site+"学的不是技术,是梦想"
            }
        }
    }
       
    )
`


```javascript
this.$emit('my-event', payload1, payload2, ...)
```

在上述代码中，`'my-event'` 是自定义事件的名称，`payload1`、`payload2` 等是可选的数据，可以传递给监听这个事件的处理器。

在你给出的代码示例中，`button-counter` 组件在被点击时会触发一个名为 `'increment'` 的事件：

```javascript
increHandler:function(){
    this.counter += 1
    this.$emit('increment')
}
```

然后，在父组件中，可以使用 `v-on` 指令（或其缩写 `@`）来监听这个事件，并指定一个处理器：

```html
<button-counter @increment="ins"></button-counter>
```

在这个例子中，当 `increment` 事件发生时，会调用 `ins` 方法，该方法将总数 `total` 增加 1。

总的来说，`$emit` 是 Vue.js 中实现自定义事件和组件间通信的关键工具。

## vue 指定

### v-if

#### v-elseif

#### v-else

### v-show

### v-on [简写为@]

### v-bind [简写为:]

### V-html [渲染原生html文件]

### v-model [适用于表单输入框]

## vue 路由

https://unpkg.com/vue-router/dist/vue-router.js
## 下载相关js数据
`wget https://unpkg.com/vue-router/dist/vue-router.js`