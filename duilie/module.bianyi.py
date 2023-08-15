#当模块第一次导入的时候，编译成解释器字节码,代码被写入一个.pyc文件，位于__pycache文目录，可以加快导入过程

#字节码缓存会自动重新生
# 成文件
import os,sys
print(123)
print(sys.path)


# 每个模块包含一个变量————name__
print(__name__) #该变量保存模块名
##解释器的顶级模块名为__main ,
# print(__main__)

if __name__=="__main__":
    print("走主程序......")
else:
    print("不走")