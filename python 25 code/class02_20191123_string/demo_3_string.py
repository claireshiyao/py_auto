# author by claire
#字符串拼接
name_one = 'bad'
name_two = 'boy'
name_full= name_one + name_two
print(name_full)  # badboy
print(name_one,name_two)  #bad boy

#字符串重复多次
name = 'badboy'
print(name * 5)

#判断字符串的长度，len()
name_three = '你好 再见'
print(len(name_three))  #5个字符
#获取字符串中的某一个字符，获取数据索引是从0开始，索引是获取某一个字符。
name_four = name_three[0]
print(name_four)  #你

#如果从左边开始数，0,1,2
#如果从右边开始数，-1，-2，-3
name_five = name_three[-1]
print(name_five)  #见

#TODO:切片，如果获取多个字符
name = '我喜欢学习'
print(name[1])
#TODO:切片用法：name[start:end:step]，取左不取右，步长默认为1
print(name[0:5:2])  #我欢习
#省略右边的，取剩下的全部
print(name[0:]) #我喜欢学习
print(name[:3]) #我喜欢
print(name[:]) #我喜欢学习

#  TODO:如果切片跳出去了，切片超出，获取剩下的所有数。
print(name[1:1000])  #喜欢学习
#如果前面超出，不会报错，也不会打印。
# TODO:如果索引超出范围，会报IndexError
print(name[1000])






