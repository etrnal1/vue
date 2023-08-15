import os
with open("duilie.py","r") as f, open("2.txt","w") as f2:
    ts=f.read()
    print(ts)


a=[1,2,3]
b=[3,4,1]

t= set(a) & set(b)
print("相同数据.........")

print(t)
ts=set(a) ^ set(b)
print("不同数据.........")
print(ts)
#在集合A中或只在集合B中的元素
# print(set(a)-set(b))

# 在集合B但不在集合A中
tt=set(b).difference(set(a))
print(tt)

# 根据您的描述，可能的原因是您在比较两列时使用的是不等于(`!=`)运算符，而不是`isin()`函数。不等于运算符会逐行比较两列，而`isin()`函数会检查一列的每个值是否存在于另一列，无关这些值的顺序。这两个操作的目标是不一样的。

# 如果你想检查B列的每个值是否存在于A列，而不是比较A列和B列的每一行是否相等，你应该使用`isin()`函数，如下所示：

# ```python
# import pandas as pd

# # 读取Excel文件
# df = pd.read_excel('filename.xlsx')

# # 用 'A' 列的值作为参考，创建一个新列 'In_A'
# df['In_A'] = df['B'].isin(df['A'])

# # 将结果保存到新的Excel文件
# df.to_excel('new_filename.xlsx', index=False)
# ```

# 在这段代码中，`df['B'].isin(df['A'])`会为每一行生成一个布尔值：如果B列的值存在于A列，它将返回`True`，否则返回`False`。然后，这个布尔值被存储在新的列'In_A'中。

# 请记住替换 `'filename.xlsx'`，`'new_filename.xlsx'`，`'A'` 和 `'B'` 为你的实际文件名和列名。

#expression for item in iterable ] #并将结果收集到列表
numbers=[1,2,3,4,5]
squares = [ n**2 for n in numbers]
print(squares)