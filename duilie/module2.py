# 导入module.py 文件
#模块文件必须放在sys.path存在的一个目录

import module
# 给模块起别名使用as
import module as mo
# 导入多个模块使用逗号分割
import os,sys,re,os
## 数据分析导入方法
import numpy as np
import pandas as pd
print(module.a)
# 为导入模块重新分配新名称，对于管理公共功能的不同实现或编写可扩展程序来说是一个有用的工具,
#如果 有两个模块unixmodule.py 和with,py。他们都定义了一个函数func(),通过编写代码来有选择的导入模块
# platform== 'unix'
# if plaform = 'unix':
#     pass
# else:
#     pass
#模块是python 中是头等对象，意味着可以赋给变量。放在数据结构中，并作为数据在程序中传递,
module.func()

#module.py 定义了一个类SomeClass,就使用名称module.SomeClass 来引用来
# 要使用单个import 来导入多个模块，请使用逗号分隔的名称列表
s=module.SomeClass()
print(s.method())
