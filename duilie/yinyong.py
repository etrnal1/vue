#当程序进行赋值时,比如b=a,就会创建一个对a的引用,
a=[1,2,3,4]
b=a
print(b is a)
b[2]=-100
print(a) #改变b的元素,
# 浅复制
print("容器对象.....")
a=[1,2,[3,4]]
b=list(a)
print(b is a)
b.append(100)
print("a 无变化")
print(a)
b[2][0]=-100
print("b的变化.......")
print(b)
print("a的变化......")
print(a)
print("a和b是单独的列表对象,但它们所半酣的元素是共享的,因此修改A的一个元素也会修改b的一个元素")