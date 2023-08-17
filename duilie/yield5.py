def flatten(items):
    for i in items:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i

#实现了内部迭代器栈,它不受递归限制,因为它将数据放在内部列表中，而不是在内部解释器中构建帧,
#生成器的延迟 计算允许改变普通函数计算的时空维度
def flattens(items):
    stack = [iter(items)]
    while stack:
        try:
            pass
            item=next(stack[-1])
            if isinstance(item,list):
                stack.append(iter(item))
            else:
                pass
                yield item
        except StopIteration:
            stack.pop()
# print(flattens([1,[2,[3,4,[5]],6]]))
for i in flattens([1,[2,[3,4,[5]],6]]):
    print(i)




