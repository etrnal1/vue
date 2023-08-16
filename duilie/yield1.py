def countdown(n):
    print('Counting down from',n)
    while n>0:
        yield n #到这停止,下次将继续调用
        # print(n)
        n -=1
        print(n)
c= countdown(10)
print("这是一个生成器.......")
print(c)
print(repr(c))
print("这是一个生成器结束.......")

next(c)


next(c)
next(c)
next(c)

# 生成器函数返回值,生成器几乎总是为for循环所用,在该循环中无法获得异常值,
#生成器的一个微妙问题是生成函数只能部分使用 ,考虑一下代码，他提前放弃了一个循环


for n in countdown(10):
    if n==2:
        break  #本例 for 循环通过break终止，相关的生成器永远不会运行到完成完成

#如果生成器函数执行某种清楚操作好呢重要，请确保使用try_finally 或上下文管理器
print("第二次使用countdown")
def countdown(n):
    print('Count2 down from',n)
    try:
        while n >0:
            yield n
            n= n-1
    finally:
        print('Only made it to',n)

print("使用上下文管理器")

def func(filename):
    with open(filename) as file:
        yield data  #代码流程到这里文件会被关闭

