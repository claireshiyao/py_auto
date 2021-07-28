"""

__file__  : 这个模块的路径

__name__ :
如果当前模块是用来作为 程序运行的脚本文件，（入口文件），
__main__ : 表示运行 python 文件的模块名。

如果不是程序运行的脚本文件，是作为模块导入其他地方的。
包名.模块名。


if __name__ == '__main__':
    pass
# 当 py 文件被作为脚本（入口）执行的时候，  if 下面的代码会执行
# 如果 py 文件是被导入其他的模块， if 下面的代码不会执行。

"""

# from class_09_import import module_1
# from class_09_import import  module_2

print(__file__)

print("主程序", __name__)


if __name__ == '__main__':
    print("hello world")



