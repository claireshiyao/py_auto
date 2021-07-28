# --*coding:utf8*--
import random
import string

print(random.sample('zyxwvutsrqponmlkjihgfedcba',5))
# ['j', 'z', 'e', 't', 'm']

print(''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 5)))
# s95L$

print(random.choice(['剪刀', '石头', '布']))
# 布

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(random.shuffle(items))
# None?
