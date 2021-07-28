# author by claire

"""
1. os
查找现在文件的绝对路径。

"""

# 获取项目路径
import os
dir_name = os.path.dirname(os.path.abspath(__file__))
print(dir_name)
root_path = os.path.dirname(dir_name)
print(root_path)

# 异常处理
try:
    print(['1'][100])
    print({"name": "yuz"}["xsy"])
except IndexError:
    print("hello")
    raise NameError
except KeyError:
    print("hello2")
# 只会出现一个错误打印
finally:
    # 无论是否保存，程序是否正常执行，都会执行语句。
    print("I like you all the time")
