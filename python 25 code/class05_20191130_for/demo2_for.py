# for 循环执行某一段程序
# 循环播放，遍历

songs = ['月亮之上','上海滩','过火','崇拜']
for song in songs:
    # song = songs[0]
    print("正在播放：{}".format(song))
    # index + 1

# 字符串也可以循环
# name = 'xsy is a girl'
# for i in name:
#     print(i,end='/')
#     # x/s/y/ /i/s/ /a/ /g/i/r/l/

# 字典
name = {"name": "xsy", "age": 18, "hobby": "sing"}
for i in name:
    print(i, end='\t')
print("")
# name	age	hobby

# 字典默认是获取keys
# 获取所有的values
# 元组解包
for i,v in name.items():
    print(i)
    print(v)
# name
# xsy
# age
# 18
# hobby
# sing

