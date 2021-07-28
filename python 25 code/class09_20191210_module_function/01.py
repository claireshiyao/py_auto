# author by claire

"""
模块：py文件
包：带有__init__.py文件的文件夹

1. 模块名称：模块名称是一个标识符
标识符命名规则：
a. 数字、下划线、字母，不能以数字开头，不能关键字
b. 一般使用下划线的形式命名，驼峰。
c. 不能和python内置的模块名称重合。
random，内置模块。

包：python3，不带__init__.py同样可以作为包使用。

2. 模块导入
from 模块名称 import 类名，函数名，变量名
适用于项目根目录/内置模块。

from (项目根目录开始)包名.包名.模块名 import 类名，函数名，变量名
自己定义的

from (项目根目录开始)包名.包名 import 模块名
使用的时候：模块名.函数名

a. 如果出现了重名的函数，那么要使用别名
b. 如果函数名称过长，也可使用别名
from 模块名称 import 类名，函数名，变量名 as alias_name

import 模块名 (as 别名)  #内置模块
调用: 模块名.函数名()
import 包名.包名.模块名

from time import time
from random import randint
print(time())
print(randint(1,99))

3.查找模块的顺序：python只能发现

模块被导入的时候
from ... import ...


"""