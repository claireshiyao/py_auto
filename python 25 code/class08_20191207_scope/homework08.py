# author by claire
"""
第一题：简单题
 1、什么是全局变量？
全局变量是在整个python文件中声明，全局范围内可以使用。

 2、什么是局部变量？
局部变量是在某个函数内部声明的，只能在函数内部使用，如果超出使用范围（函数外部），则会报错。

 3、函数内部如何修改全局变量（如何声明全局变量 ）？
如果想在函数内部改变全局变量，需要在前面加上global关键字，在执行函数之后，全局变量值也会改变。

 4、写出已经学过的所有python关键字，分别写出用途？
False: 假，布尔属性值。一般是判断检测的属性。
True: 真，布尔属性值。一般是判断检测的属性。
None: 如果一个函数没有返回值，那解释器就默认它的返回值是None。None 常用于 assert、判断以及函数无返回值的情况。
and: 用于表达式运算、逻辑与操作。
break: 结束整个循环。
continue: 跳出当前循环，即终止此次循环接下来的指令，进行下次循环。
def: 用于自定义函数、方法。
del: 可用于删除列表、字典的元素，也可以用于删除变量。
elif: 用于If语句分支结构，若if条件不满足，则执行elif。
else: 用于If语句分支结构，若if,elif所有判断条件都为假，则执行else分支下的执行语句。
for: 用于for循环。
from: 用于导入模块，与import一起使用。
global: 定义全局变量。
if: 用于if条件语句。
import: 用于导入模块，与from一起使用。
in: 判断变量是否在列表中。
not: 用于表达式运算，逻辑非操作。
or: 用于表达式运算，逻辑或操作。
pass: 函数占位符。
return: 用于函数返回结果。
while: 用于while循环语句。
"""


# 第二题：数据转换
# 有一组用例数据如下：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

# 要求一：把上述数据转换为以下格式
# res1 = [
#     {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
#     {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
# ]
res1 = []
for i in range(1, len(cases)):
    d = dict(zip(cases[0], cases[i]))
    res1.append(d)
print(res1)

# 要求二：把上面转换好的数据中case_id大于3的用例数据获取出来,得到如下结果
# res = [
#     {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
# ]
res = []
for j in res1:
    if j['case_id'] > 3:
        res.append(j)
print(res)

# 第三题：画出函数相关内容的思维导图或者笔记。