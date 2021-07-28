# author by claire

def sum(a, b):
    total = 0
    c = total + a + b
    return c

def sum_total(a, b, *args, **kwargs):
    """**kwargs表示接收多余的关键字参数"""
    # 函数体内kwargs是字典的形式接收多余的关键字参数
    print(kwargs) # {'name': 'xsy', 'age': 18}
other_info = {"hobby":"girl","food":"巧克力"}
sum_total(3,4,5,6,name='xsy',age=18,**other_info)
# {'name': 'xsy', 'age': 18, 'hobby': 'girl', 'food': '巧克力'}

"""
总结：
函数的返回值：return, return语句之后的语句不生效。
函数的参数：
1. 位置参数：一个萝卜一个坑
2. 关键字参数：好记，可换顺序
3. 默认参数：可少传参数
4. 注意：顺序：位置参数，关键字参数和默认参数在后面

不定长参数：动态参数
1. 位置参数：*args,函数体和函数外面
2. 关键字：**kwargs
"""