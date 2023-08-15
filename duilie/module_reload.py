import importlib
import module
#reload()工作方式是加载新版本的模块源代码。然后在已经存在的模块命名空间执行，
importlib.reload(module)
print(loaded(module))