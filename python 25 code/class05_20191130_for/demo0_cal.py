# 数据运算
# 算术运算  加减乘除
# +  -  *  /
print(1 + 1)

# 除法运算，跟python版本有关系，算完以后是float类型
print(type(900/3))  # <class 'float'>

# 整除
print(5//3)  # 1

#  取余，%，模运算
print(8 % 5)  # 3

# 幂运算**
print(2**4)  # 16

# 浮点数运算不能精确
# 0.1 + 0.2 = 0.30000000000004
# 如果要去测试，预期结果是100.1，结果花费了0.3元，实际结果99.8
# 100，1 - 0.2 = 99.8999999999
from decimal import Decimal
print(100.1-0.2)  # 99.89999999999999\
# Decimal能够维持很高的精度
# Decimal函数里是字符串形式，不要写成数字形式
print(type(Decimal('100.1') - Decimal("0.2")))  # <class 'decimal.Decimal'>
print(Decimal("100.1") - Decimal("0.2") == Decimal("99.9"))  # True

# 赋值运算 +=  -=  *= /=
name = 'xsy'
name += 'xie'
print(name) # xsyxie

age = 500
age -= 1
print(age)  # 499

# 比较运算  >  <  ==  !=  >=  <=
# TODO:比较运算等于符号是2个=，一个=是赋值
# 比较运算得到的结果是布尔值
[print(1 == 3-2)] # True
print(4 != '4')  # True,数字不等于字符串

# 逻辑运算 and not or
# and并且
print(1 == 1 and 2 == 3) # False
# or 或者
print(1 == 1 or 2 == 3) # True,只要有一个为真，就是真


# not 非，取反
print(not (1 == 1 or 2 == 3))   # False
# 优先级，不要记忆
# 提高优先级
# 逻辑运算的结果是布尔值
print(not (1 == 1) or (2 == 3))  # False

# 成员运算
# in not in
# 字符串，列表，字典，元组
print("yuz" in "yuz wang")  # True
print(3 not in [1,2,3])  # False

# TODO: 字典的in是判断key值，不是value
print('xsy' in {"name":"xsy","age":18})  # False
print({"name":"xsy","age":18}.values())  # dict_values(['xsy', 18])
print('xsy' in {"name":"xsy","age":18}.values())  # True









