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
    def __init__(self,start)
        self.start=start
    def __iter__(self):  #每次迭代是,__iter__()都会创建一个新的生生成器
        n=self.start
        while n>0:
            yield n
            n-=1