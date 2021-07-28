# author by claire
str1 = 'python cainiao 6666'
#  1、请找出第 5 个字符。
print(str1[4])
# 2、请复制一份字符串，保存为 str_two
str_two = str1[0:]
print(str_two)
# 3、请找出最中间的字符。（字符串长度是奇数。）
print(str1[int((len(str1)-1)/2)])
# 请找出最中间的字符。（字符串长度是偶数。）
middle = int(len(str1)/2)
print(str1[middle-1])
print(str1[middle])
# 4、选做：有基础的同学可以尝试字符串长度不确定的情况。(涉及到后面内容，不需要提交)

# 卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！
#（不需要校验数据，都传入数字就可以了。）
price = input("请输入橘子的价格：")
weight = input("请输入橘子的重量：")
print(float(price)*float(weight))

my_hobby = "Never stop learning!"
# 截取从 位置2 ~ 位置6 的字符串
print(my_hobby[1:6])
# 截取从 位置2 ~ 末尾 的字符串
print(my_hobby[1:])
# 截取从 开始位置~ 位置6 的字符串
print(my_hobby[:6])
# 截取完整的字符串
print(my_hobby[:])
# 从 索引3 开始，每2个字符中取一个字符
print(my_hobby[3::2])
# 从右边开始截取，倒数第 2位置 到 倒数 5位置，步长为2
print(my_hobby[-2:-6:-2])
# 截取字符串末尾两个字符
print(my_hobby[-2:])
# 字符串的逆序
print(my_hobby[-1::-1])
