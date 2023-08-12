typora-root-url: ./image

# docker 安装gitlab和打包gitlab


要将 Docker 镜像部署在内网中，你通常需要以下步骤：

1. **在可以访问外网的机器上下载镜像**

   在可以访问外网的机器上，使用 `docker pull` 命令下载你需要的 Docker 镜像：

   ```bash
   docker pull registry.cn-hangzhou.aliyuncs.com/lab99/gitlab-ce-zh
   ```

2. **保存镜像到一个文件**

   使用 `docker save` 命令将 Docker 镜像保存为一个 tar 文件：

   ```bash
   docker save -o gitlab-ce-zh.tar registry.cn-hangzhou.aliyuncs.com/lab99/gitlab-ce-zh
   ```

   这将会创建一个名为 `gitlab-ce-zh.tar` 的文件，该文件包含了 Docker 镜像的所有层。

3. **将镜像文件复制到内网机器**

   将 `gitlab-ce-zh.tar` 文件复制到你的内网机器上。你可以使用任何传输文件的方式，例如 SCP、FTP、物理介质等。

4. **在内网机器上加载镜像**

   在内网机器上，使用 `docker load` 命令从 tar 文件中加载 Docker 镜像：

   ```bash
   docker load -i gitlab-ce-zh.tar
   ```

5. **在内网机器上运行 Docker 容器**

   使用 `docker run` 命令在内网机器上运行 Docker 容器。请确保你的命令中的所有路径和设置都是正确的，例如你的 GitLab 配置文件、数据和日志的存储位置。

   ```bash
   sudo docker run --detach --publish 8443:443 --publish 8090:80  --publish 8022:22  --name gitlab   --restart always --hostname 127.0.0.1  -v /path/to/gitlab/etc:/etc/gitlab -v /path/to/gitlab/logs:/var/log/gitlab  -v /path/to/gitlab/Users/mac:/var/opt/gitlab -v /etc/localtime:/etc/localtime:ro --privileged=true registry.cn-hangzhou.aliyuncs.com/lab99/gitlab-ce-zh
   ```

   在这个命令中，你需要替换 `your-hostname` 和 `/path/to/gitlab/` 等为你实际的主机名和路径。

   <!-- 原版 -->
   sudo docker run --detach --publish 8443:443 --publish 8090:80  --publish 8022:22  --name gitlab   --restart always --hostname 127.0.0.1  -v /Users/mac/software/gitlab/etc:/etc/gitlab -v /Users/mac/software/gitlab/logs:/var/log/gitlab  -v /Users/mac/software/gitlab/data:/var/opt/gitlab -v /etc/localtime:/etc/localtime:ro --privileged=true registry.cn-hangzhou.aliyuncs.com/lab99/gitlab-ce-zh  

   启动完以后 页面无法正常访问，我该如何排查


    ## 安装针对mac M2,m1版本的镜像
    docker pull ozhrm8gx.mirror.aliyuncs.com/yrzr/gitlab-ce-arm64v8


        docker pull ozhrm8gx.mirror.aliyuncs.com/yrzr/gitlab-ce-arm64v8


        docker run -itd -p 9980:80 -p 9922:22 -v /usr/local/gitlab-test/etc:/etc/gitlab -v /usr/local/gitlab-test/log:/var/log/gitlab -v /usr/local/gitlab-test/opt:/var/opt/gitlab --privileged=true --name gitlab-test gitlab/gitlab-ce


        您的SQL查询有几个问题，这可能是导致语法错误的原因。我将逐一地对这些问题进行解析，然后提供一个修改后的查询语句。

1. **`distinct(device_name)`**：`DISTINCT`通常用来消除结果集中的重复行。在`SELECT`子句中，`DISTINCT`应该放在所有列名之前，而不是单列。在此，您似乎想要得到唯一的`device_name`，但是在`SELECT`子句中如此使用`DISTINCT`是不正确的。

2. **`GROUP BY caputure_time`**：在`GROUP BY`子句中，您应该只包含那些您希望在结果集中进行分组的列。在您的查询中，您想要根据`caputure_time`进行分组，但是您也在`SELECT`子句中包含了`name`和`device_name`。如果这些列在每个`caputure_time`下都具有唯一值，那么您需要在`GROUP BY`子句中包含这些列。

3. **正则表达式**：在MySQL中，`REGEXP`是一个比较运算符，用于匹配正则表达式。您的正则表达式看起来是正确的，前提是您想要匹配包含"进"或"出"的`doorway`。

考虑到上述问题，以下是修改后的查询：

```sql
SELECT name, device_name, caputure_time
FROM faceregont 
WHERE name ='梁旭' AND doorway REGEXP '进|出' 
GROUP BY name, device_name, caputure_time
ORDER BY caputure_time
```

这个查询将返回`name`为"梁旭"，且`doorway`包含"进"或"出"的每一行，每行包含唯一的`name`，`device_name`，和`caputure_time`组合。结果将按`caputure_time`排序。
    
如果您希望获取每天的最早和最晚时间，您可以使用`DATE()`函数将`caputure_time`转换为日期，然后使用`MIN()`和`MAX()`函数来获得每天的最早和最晚的时间。以下是一个示例的SQL查询语句：

```sql
SELECT 
  DATE(caputure_time) as date,
  MIN(caputure_time) as earliest_time,
  MAX(caputure_time) as latest_time
FROM faceregont
GROUP BY DATE(caputure_time)
ORDER BY date;
```

这个查询首先将`caputure_time`转换为日期，然后按日期分组。对于每个日期，查询返回最早的`caputure_time`（即该日期的最早时间）和最晚的`caputure_time`（即该日期的最晚时间）。最后，结果按日期排序。

请注意，这个查询假设您的`caputure_time`字段是一个时间戳或日期时间类型的列。如果不是，您可能需要先将该字段转换为适当的类型再进行这些操作。



# vue 学习[包含es6语法]

## vue 常用词汇
component
data
methods 
template 
$emit
increment
v-on  简写 @
v-bind 简写:

fillte

## vue 数据示范

Vue 构造器中有一个el 参数，它是 DOM 元素中的 id
data 用于定义属性，实例中有三个属性分别为：site、url、alexa。
methods 用于定义的函数，可以通过 return 来返回函数值。
{{ }} 用于输出对象属性和函数返回值。

```vue
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
```



## vue 基本语法

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


## 




## npm  [工具的使用]

build   项目构建webpack 代码

config  配置目录,包括端口号

Node_modules npm加载的项目依赖模块

src     这是我们要开发的目录

static  静态资源 

test   初始test 目录

  index

Package.json 项目配置文档

README.md

.browserslistic 配置浏览器的兼容性
gitignore 配置git忽略文件,用于告诉git哪些文件不需要被添加到版本管理中,例如项目的node_modules依赖包的代码,该文件会占用很大的内存,一般不会提交到远程仓库,提交的代码时会忽略该文件夹

1. Node_modules

  

1. package.json

## 文件结构

template HTML 元素内容,用于定义Vue.js组件的

​     模版内容,数据渲染,UI组件等

Script 页面业务逻辑，比如生命周期,函数,组件,监听

style  样式层

## 项目入口

Vue.js 是单页面应用

开发环境运行项目执行npm run serve,该命令行是package.json文件script下的serve,



入口 npm run serve 开始执行src/main.js 文件,在main.js文件创建Vue.js实例,并引入根组件App.vue.然后再Vue.js实例中注入router和store,最后调用.mount方法将Vue.js实例挂载到index.html文件中id为App的DOM元素挂载点



## 路由

Import Home from "../views/Home.vue"

- import 导入
- from  来源于
- @ 符号指向src 目录



### 项目初始化配置

Src/views/Home.vue组件,看看在浏览器有什么变化

### 配置vue.config.js

Vue.config.js 是一个可选的配置文件，

### 使用element Plus组件库

对于Web应用来说,只使用原生的DOM元素,往往无法满足项目的需求,如input,select,textatea等,因为他们的功能不够强大,在开发过程使用原生dom元素会非常吃力,不仅要实现开发元素之间的交互,还要让元素的Ui效果达到统一,使用第三方UI 是首选项,引入组件的方式,完整导入,按需自动导入,按需手动导入,

- ## 完整导入

- ## 按需自动导入

- 按需手动导入

 Elment Plus 组件很多,如果导入的组件非常多,会导致main.js文件代码混乱,为了更好地管理element Plus 组件,可以将组件作为独立的文件,将不同的功能剥离出来



src/main.js

`import ElementPlus from 'elment-plus'`

`import 'element-plus/dist/index.css'`

​									

- 遇见问题 npm 不能安装element-plus

  ```js
  pm ERR! code ERESOLVE
  npm ERR! ERESOLVE unable to resolve dependency tree
  npm ERR!
  npm ERR! While resolving: vue_test@1.0.0
  npm ERR! Found: vue@2.7.14
  npm ERR! node_modules/vue
  npm ERR!   vue@"^2.5.2" from the root project
  npm ERR!
  npm ERR! Could not resolve dependency:
  npm ERR! peer vue@"^3.2.0" from element-plus@2.3.8
  npm ERR! node_modules/element-plus
  npm ERR!   element-plus@"*" from the root project
  npm ERR!
  npm ERR! Fix the upstream dependency conflict, or retry
  npm ERR! this command with --force or --legacy-peer-deps
  npm ERR! to accept an incorrect (and potentially broken) dependency resolution.
  npm ERR!
  npm ERR!
  npm ERR! For a full report see:
  npm ERR! /Applications/MxSrvs/cache/nodejs/_logs/2023-07-26T05_24_21_847Z-eresolve-report.txt
  
  npm ERR! A complete log of this run can be found in: /Applications	/MxSrvs/cache/nodejs/_logs/2023-07-26T05_24_21_847Z-debug-0.log
  
  
  
  
  ```

  

sudo npm install vue@3
sudo npm install element-plus --save

## vue  ui 

![Snipaste_2023-07-26_14-03-49](/Snipaste_2023-07-26_14-03-49.png)





### vue 运行





![vue运行](file:../vue/image/vue%E8%BF%90%E8%A1%8C.png)

## 路由 【将组件(components)映射到路由路径(routes)】
### vu3 打包

cnpm run build 会在vue目录下生成dist 目录,该目录一般包含index.html文件以及static目录,static目录包含了静态文件js,css以及图片目录images 如果有图片的话

build  项目构建 webpack 代码

config 配置目录,包括端口号鞥

Node_modules npm 加载的项目依赖模块

Src 开发的目录

​	  assets 放置图片logo

​      components 目录放的组件

​     App.vue 项目入口文件,可以直接写组件在里面

   main.js 项目的核心文件

index.css 样式文件

static 静态资源
public 公共资源

test 初始测试目录,可删除

.xxxx文件 配置文件 语法配置,git配置

Index.html 项目配置文件

README.md 项目的说明文档

dist npm run build 命令会生成该目录

### es6 语法规范

Es6 模块化

包管理器

原型,原型链

数组常用方法

 过滤数组,加工数组

axios

promise



### node

  Node.js 运行es6

#### Webpack

​     是一个现代Javascript 应用程序的静态模块打包器,当webpack处理应用程序时,它会递归底构建一个依赖关系图

 入口

输出

Loader

插件(plugins)

## es5

错误信息 "Cannot use import statement outside a module" 在 Node.js 中试图使用 ECMAScript 模块（ESM）时是一个常见的错误。

默认情况下，Node.js 将 `.js` 扩展名的文件视为 CommonJS 模块。`import` 语句是 ECMAScript 模块的一部分，不适用于 CommonJS 模块。所以当你在 `.js` 文件中使用 `import`，Node.js 就会抛出 "Cannot use import statement outside a module" 的错误。

你有几种不同的选项来解决这个问题：

1. **将你的文件重命名为 `.mjs`**：Node.js 默认将 `.mjs` 文件视为 ESM。所以你可以将你的文件从 `.js` 重命名为 `.mjs`，它应该就可以工作了。

```bash
mv es6mokuaiimport.js es6mokuaiimport.mjs
```

然后你可以用 Node.js 运行文件：

```bash
node es6mokuaiimport.mjs
```

2. **使用 `--experimental-modules` 标志**：你可以通过使用 `--experimental-modules` 标志告诉 Node.js 将 `.js` 文件视为 ESM。

```bash
node --experimental-modules es6mokuaiimport.js
```

3. **在你的 `package.json` 中设置 `"type": "module"`**：告诉 Node.js 将 `.js` 文件视为 ESM 的另一种方式是在你的 `package.json` 中包含 `"type": "module"`。

```json
{
  "name": "my-package",
  "version": "1.0.0",
  "type": "module",
  "main": "es6mokuaiimport.js"
}
```

然后你可以用 Node.js 运行文件：

```bash
node es6mokuaiimport.js
```

请注意，使用 ECMAScript 模块在 Node.js 中仍然是实验性的，未来版本中的行为可能会发生变化。




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

## Es6

### let [es6 新增关键字 let 和const]

```
//let 只能声明一次,var只能声明全部  var 变量提升,let没有
```

### const 声明一个常量不能修改

### for

#### 下面的for循环代码为什么输出10

这是因为JavaScript采用的是基于事件循环的并发模型，这种模型中，一些代码（如 `setTimeout`，`setInterval` 或 AJAX 请求等）是异步执行的，这意味着它们不会立即执行，而是在当前执行栈中的所有同步代码执行完毕后才会执行。

// 在你的代码中，`for` 循环是同步代码，而 `setTimeout` 是异步代码。因此，`for` 循环会首先完全执行，然后所有的 `setTimeout` 回调才会执行。由于 `setTimeout` 没有设置延迟时间，它会尽快执行，但总是在所有同步代码之后。

// 简单来说，`setTimeout` 延迟的不仅仅是它的回调函数，还包括所有的同步代码。这就是为什么在这个例子中，所有的 `setTimeout` 都在 `for` 循环结束后才执行的原因。

// 下面是一个简单的时间线来描述这个过程：

// 1. `for` 循环开始执行。

// 2. 每次迭代，都会调度一个 `setTimeout`，但是这些 `setTimeout` 的回调并不会立即执行，而是被添加到一个队列中等待执行。

// 3. `for` 循环结束后，`i` 的值变为 `10`。

// 4. 此时，所有的同步代码都已经执行完毕，事件循环开始处理队列中的 `setTimeout` 回调。

// 5. 每个 `setTimeout` 回调函数访问变量 `i`，此时 `i` 的值已经是 `10`。

// 这就是为什么所有的 `setTimeout` 回调都打印出 `10` 的原因。

```js
for(let i =0;i<10;i++){
    setTimeout(function(){
        console.log("let 函数的使用",i)
    })

}
```



### array

- Array.from
- array.like
- mapFn
- thisArg
- 转换map
- 转换set
- 转换字符串
- find [查找返回符合条件的第一个]
- findIndex
- fill
- CopyWithin()
- Entries [遍历键值对]
- keys 遍历键名
- values 遍历值
- includes 包含某值
- Flat() 嵌套数组转换为一堆数组
- flatMap() 先对数组中每个元素进行处理，在对数组执行flat()方法

### func

### class

### Import 与export

### mjs

### 异步编程  promise 

[有三种状态] pending  fulfilled rejected



 promise  对象只有 : 从pending 变为fulfilled 和从pending 变为rejected的状态更改,只要处于fulfilled 和rejected ,状态就不会再变了即resolved(已经定型)

#### then 方法

then 方法接收两个函数作为参数,第一个参数是Promise执行成功时回调,第二个参数是Promise执行失败时的回调,两个函数只有一个被调用

````js
这段代码创建了两个 Promise 对象 `p1` 和 `p2`，然后使用 `then` 方法来处理这两个 Promise 的结果。

在这段代码中，`p1` 和 `p2` 都是 Promise 对象。Promise 是 JavaScript 中的一种内置对象，它用于处理异步操作。Promise 对象表示一个异步操作的最终完成（或失败）及其结果值。

Promise 对象接受一个函数作为参数，这个函数接收两个参数，通常命名为 `resolve` 和 `reject`。`resolve` 函数在异步操作成功时被调用，并接收异步操作的结果作为参数；`reject` 函数在异步操作失败时被调用，并接收错误信息作为参数。

```javascript
const p1 = new Promise(function(resolve, reject){
    resolve('success2');
    reject('reject');
});
```

在这个示例中，`resolve` 函数被调用并传入 `success2` 作为结果。然后 `reject` 函数被调用，但是在 Promise 中，一旦调用了 `resolve` 或 `reject`，Promise 的状态就会改变，且无法再次改变。所以在这个例子中，`reject('reject')` 这行代码实际上并没有任何效果，因为 `resolve` 已经被调用过了。

接下来，`then` 方法被调用来处理 Promise 的结果。`then` 方法接受两个参数，两个参数都是函数。第一个函数是 Promise 被解决（即异步操作成功）时的回调函数，第二个函数是 Promise 被拒绝（即异步操作失败）时的回调函数。

```javascript
p1.then(function(value){console.log(value)});
```

在这个示例中，只提供了第一个参数，即 Promise 被解决时的回调函数。所以当 `p1` 被解决时，会输出 `success2`。

同样，在 `p2` 中，虽然调用了 `reject('reject')`，但因为 `resolve('success3')` 先被调用，所以 `p2` 也是解决的状态，会输出 `success3`。

这段代码中的一个重要点是，即使 `reject` 函数被调用，但是由于 `resolve` 函数先被调用，Promise 的状态已经改变，因此 `reject` 的调用不会改变 Promise 的状态。这就是为什么这段代码会输出 `success2` 和 `success3`，而不是抛出任何错误的原因。
````


这个错误信息表明你的文件`router.config.js`在第26行存在尾随空格。ESLint规则`no-trailing-spaces`不允许行尾有空格。

### 解决方案

你可以手动修复这个问题，也可以使用ESLint的`--fix`选项自动修复。

#### 手动修复

1. 使用代码编辑器打开文件`router.config.js`。
2. 跳转到第26行。
3. 删除该行末尾的任何空格。
4. 保存文件。

#### 自动修复

运行以下命令：

```
./node_modules/.bin/eslint --fix /Users/mac/vue/ffmpeg/frontend/my-project/src/config/router.config.js
```

此命令告诉ESLint自动修复指定文件中可以修复的问题。

### 防止未来的问题

为了防止未来出现这样的问题，你可以配置你的代码编辑器在保存文件时自动删除尾随空格。例如，在Visual Studio Code中，你可以添加以下设置：

```json
{
    "files.trimTrailingWhitespace": true
}
```

此外，建议在提交代码或作为CI过程的一部分时运行你的linter，以便在代码被提交或推送到你的仓库之前捕获这些问题。Husky和lint-staged等工具可能对此有所帮助。

