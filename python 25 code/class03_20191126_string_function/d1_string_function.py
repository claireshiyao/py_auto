# author by claire
# 变量命名：
my_string = '今晚你那里下雪了吗？面对寒冷你怕不怕'

# 获取长度 len()
my_string = 'snow now'

# 转化成大写
print(my_string.upper())
# 转化成小写
print(my_string.upper().lower())
# 大小写互换
new_string = 'Snow Beauty'
print(new_string.swapcase())

# 首字母大写title()，capitalize()
# 查找，查找不到的时候，find会返回-1
# 当find查找到指定的元素时候，返回开始的字母的索引值。
# 必须是连续的字符
if_snow = my_string.find('w n')
print(if_snow)

# index和find的作用类似
# 不同：值错会报错ValueError
# IndexError：索引错误
# if_snow = my_string.index('wn')
# print(if_snow)

# 替换replace
# 字符串一旦定义，除非重新复制，不然不会发生变化
dalao_name = '本本'
new_dalao = dalao_name.replace('本','丢',1)
print(dalao_name) #本本
print(new_dalao) #丢本；只改1个。

# 统计
song = '理想啊，理想，我的理想，永远那么年轻啊啊啊啊，理想'
print(song.count('理想'))

# join，字符串拼接，正规方式，代替+
song_1 = '理想啊，理想，'
song_2 = '我的理想，'
song_3 = '永远那么年轻啊啊啊啊'
song_total = '++++++'.join([song_1,song_2,song_3])
print(song_total)
#理想啊，理想，++++++我的理想，++++++永远那么年轻啊啊啊啊

# 字符串分割
print(song_total.split('++++'))
# ['理想啊，理想，', '++我的理想，', '++永远那么年轻啊啊啊啊']

# strip 去掉左右两边的指定字符串
girl = '心拼命姑娘心'
print(girl.strip('心'))

# 如果左右两边不一样
girl = '男拼命姑娘儿'
print(girl.lstrip('男')) #拼命姑娘儿
print(girl.rstrip('儿')) #男拼命姑娘
print(girl.lstrip('男').rstrip('儿'))  #拼命姑娘

# 判断是否是一个正整数，经常使用
a = '-2345'
print(a.isdigit())  #False



