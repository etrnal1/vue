from datetime import date
d =date(2012,12,21)
print(d)
# repx 创建一个对象表示字符串,
print(repr(d))


print(f'th date is: {d!r}')
#在字符串格式化中 将!r后缀添加到值来生成repr值,以区别常规的字符串转换
#头等对象
#python 中的所有对象都是头等对象,对象可以被当做变量存储，

items ={
    'number':42,
    'text':"hello world"
}
print(items)
items['func'] =abs
import math
items['mod'] =math
nums =[1,2,3,4]
items['append'] = nums.append
print(items)
print("调用函数........")
print(items['func'](-45))
print("math 函数.....")
print(items['mod'].sqrt(4))
#Python 中的所有内容都是头等性的,可以利用该特性来编写紧凑和额灵活的代码

line='ACME,100,490.10'
column_types=[str,int,float]
parts = line.split(',')
print(line)
row= [ty(val) for ty,val in zip(column_types,parts)]
print(row)

## 字典示例
_formats={
    'text':'TextFormatter',
    'csv':'CSVFormatter',
    'html':'HTMFormatter'
}
if format in _formats:
    formatter=_formats[format]()
else:
    raise RuntimeError('Bad Format')