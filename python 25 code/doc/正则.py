# author by claire

"""
match
findall
search

"""

# 匹配特定的字符串"abc"
import re
re_pattern = r'abc'

# 从字符串当中匹配是否有abc
# match表示从开始位置进行匹配
res = re.match(re_pattern, "rfwcabcdef")

# search 全文匹配，只匹配一次
res = re.search(re_pattern, "abcrfwcabcdef")

# findall, 全部匹配
res = re.findall(re_pattern, "abcrfwcabcdef")

# 匹配手机号码
re_pattern = r'1[35789]\d{9}'


