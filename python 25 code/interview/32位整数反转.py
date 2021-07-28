# coding:utf-8
# 2、给出一个32位的有符号整数，将整数每位上的数字进行反转
import random

list_one = []
for i in range(1, 33):
    list_one.append(str(random.randint(1, 9)))
symbol = random.choice(["", "-"])
num = symbol + "".join(list_one)
print(num)

if num[0] != "-":
    new_num = int(num[::-1])
else:
    new_num = -int(num[:0:-1])
print(new_num)
print(type(new_num))

