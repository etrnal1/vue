#模块缓存
#不管使用Import 语句多少次，模块和源代码都只加载和执行一次，
import sys
# print(sys.modules)
#在函数中使用import
def f(x):
    import math
    return math.sin(x)+math.cos(x)

    # comment:
print(f(10))
#从模块导入选定名称 [从模块缓存到本地命名空间的名称复制]
# from module import func  #导入module并将func放到当前命名空间中，python 首先在幕后执行import module, 然后缓存到一个本地名称进行赋值

name=sys.modules['os'].name
print("打印模块名字......")
print(name)
#无论哪种方式,整个模块都被加载并储存在缓存中,

from module import func
a=42
func()

print("函数模块名",func.__module__)
print(func.__globals__['a'])