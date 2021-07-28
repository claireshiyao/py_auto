# while True:
#     print("I LOVE YOU")  # 无限循环

# while (条件表达式):
i =  0
while (i<10):
    print("I LOVE YOU")
    print(i)
    i += 1
print("I LOVE YOU TOO")

j = 0
while True:
    print("我喜欢你")
    if j == 5:
        print("我不喜欢你了")
        print(j)
        break  # 退出循环
    j += 1
    continue # 退出这个条件,进入下一个分支
print("爱的太卑微")


# 嵌套循环
my_list = [('a','b'),('c','d')]
for name in my_list:
    print(name)
    for k in name:
        print(k)

list_1 = [4,5,6]
list_2 = [2,3,4]
for v1 in list_1:
    for v2 in list_2:
        print("{} + {} = {}".format(v1,v2,v1 + v2))
# 4 + 2 = 6
# 4 + 3 = 7
# 4 + 4 = 8
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 6 + 2 = 8
# 6 + 3 = 9
# 6 + 4 = 10


