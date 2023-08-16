# 通常生成器执行一次
def countdown(n):
    print('Count2 down from',n)
    try:
        while n >0:
            yield n
            n= n-1
    finally:
        print('Only made it to',n)
c=countdown(3)
for n in c:
    print('T-minus',n)


#如果想要一个允许重复迭代的对象，将其定义为一个类并设置让__iter()__方法成为生成器


class countdown:
    def __init__(self,start):
        self.start=start
    def __iter__(self):  #每次迭代是,__iter__()都会创建一个新的生生成器
        n=self.start
        while n>0:
            yield n
            n-=1

# 生成器委托
##生成器的基本特性，涉及到yield不会自动执行,除非调用next()和for循环

def countup(stop):
    n=1
    while n<=stop:
        yield n
        n+=1

def countdown(start):
    n=start
    while n>0:
        yield n
        n-=1

def up_and_down(n):
    yield from countup(n) 
    yield from countdown(n)

#yield from 有效地将迭代过程委托给外部迭代

for x in up_and_down(5):
    print(x,end='')