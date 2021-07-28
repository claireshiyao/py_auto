#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽

"""
正则表达式是一种通用的字符串匹配技术，是不会因为编程语言不一样而发生变化的。
想要查找某种特征的，具有一定规则的字符串，都是可以尝试使用正则表达式。
jsonpath, xpath, 解析相关。

匹配的方式: 只是 python 当中的封装， re
- match
- search
- findall

discover

"""

# 匹配特定的字符串  "abc"
import re
# re_pattern = r'abc'

# 从 "wofowpqfowfjowefjiwoefabcowof" 这个字符串当中匹配是否 有 re_pattern
# match 表示： 从开始的位置进行匹配
# res = re.match(re_pattern, "abwofowpqfowfjowefjiwoefabcowof")
# print(res)

# search, 全文匹配
# res = re.search(re_pattern, "abcwofowpqfowfjowefjiwoefabcowof")
# print(res)

# findall, 全部匹配
# res = re.findall(re_pattern, "abcwofowpqfowfjowefjiwoefabcowof")
# print(res)


# [abc], 匹配中括号中的而任意一个字符
# re_pattern = '{m, n}',
# res = re.findall(re_pattern, "abcwofowpqfowfjowefjiwoefabcowof")
# print(res)

# [a-z], 匹配中括号中的而任意一个字符
# re_pattern = '{m, n}',
# res = re.findall(re_pattern, "abcwofowpqfowfjowefjiwoefabcowof")
# print(res)



# . 匹配任意的一个字符串， 除了 \n
# re_pattern = r'.'
# res = re.findall(re_pattern, "a\nbcwofowpqfowfjowefjiwoefabcowof")
# print(res)


# \d  匹配数字 data
# re_pattern = r'\d'
# res = re.findall(re_pattern, "a123bcwofowpqfowfjowefjiwoefabcowof")
# print(res)

# \D  匹配非数字 data
# re_pattern = r'\D'
# res = re.findall(re_pattern, "a@123bcwofowpqfowfjowefjiwoefabcowof")
# print(res)

# \w  匹配字母，数字，下划线
# re_pattern = r'\w'
# res = re.findall(re_pattern, "a@_123bcwofowpqfowfjowefjiwoefabcowof")
# print(res)

# \W 反向的， 非


#  匹配花括号当中的数字次，  匹配几次，
# re_pattern = r'\d{2}'
# res = re.findall(re_pattern, "aa@_123b&cwofowpqfowfjowefjiwoefabcowof")
# print(res)

#  {2, } 匹配至少 2 次
# TODO: 正则表达式当中，千万不要手残，空格不能随便打
# 贪婪模式， python 当中
# re_pattern = r'\w{2,}'
# res = re.findall(re_pattern, "aa@_123b&cwofowpqfowfjowefjiwoefabcowof")
# print(res)



# {,2} 匹配最多 2 次
# re_pattern = r'\w{,2}'
# res = re.findall(re_pattern, "aa@_123b&cwofowpqfowfjowefjiwoefabcowof")
# print(res)


# {2,4} 匹配 2 -4 次
# re_pattern = r'\w{2,4}'
# res = re.findall(re_pattern, "aa@_123b&cwofowpqfowfjowefjiwoefabcowof")
# print(res)

# 如何去匹配一个手机号码
# re_pattern = r'1[35789]\d{9}'
# res = re.findall(re_pattern, "aa@_123b&cwo17520208510fowpqfowfjowefjiwoefabcowof")
# print(res)

# 邮箱号码？

# # * 匹配 0 次或者任意次, 通配符，
# re_pattern = r'\d*'
# res = re.findall(re_pattern, "aa@_123b&cwo17520208510fowpqfowfjowefjiwoefabcowof")
# print(res)

# +  匹配 1 次或者任意次, 通配符，
# re_pattern = r'\d+'
# res = re.findall(re_pattern, "aa@_123b&cwo17520208510fowpqfowfjowefjiwoefabcowof")
# print(res)

# 组合
# re_pattern = r'\d.'
# res = re.findall(re_pattern, "aa@_123b&cwo17520208510fowpqfowfjowefjiwoefabcowof")
# print(res)


# # ? 匹配 0 次或者 1 次
# re_pattern = r'\d?'
# res = re.findall(re_pattern, "aa@_123b&cwo17520208510fowpqfowfjowefjiwoefabcowof")
# print(res)


# # ?非贪婪模式, 尽量少的匹配
# re_pattern = r'\d*?'
# res = re.findall(re_pattern, "aa@_123b&cwo17520208510fowpqfowfjowefjiwoefabcowof")
# print(res)


# ^ 开头
# re_pattern = r'^\d'
# res = re.findall(re_pattern, "1aa@_123b&cwo17520208510fowpqfowfjowefjiwoefabcowof")
# print(res)
#
# # ^ 结尾
# re_pattern = r'\d*$'
# res = re.findall(re_pattern, "jiwoefabcowof3434")
# print(res)
#
#
# mystr = '{"member_id": "#member_id#", "loan_id": "#loan_id#", "token": "#token#", "username": "#username#"}'
# # 匹配规则
# re_pattern = r'#(.*?)#'
# res = re.findall(re_pattern, mystr)
# print(res)
#
# # 组
# # 替换 re.sub() 替换操作
# mystr = re.sub(re_pattern, 'me123', mystr, 1)
#
# mystr = re.sub(re_pattern, 'loan123', mystr, 1)
#
# mystr = re.sub(re_pattern, 'tokenloan123', mystr, 1)
#
# print(mystr)

class Context:
    member_id = 888
    loan_id = 777
    token = 'aofoweflsf'
    username = 'yuz'


def replace_label(target):
    """while 循环"""
    re_pattern = r'#(.*?)#'
    while re.findall(re_pattern, target):
        # 如果能够匹配
        key = re.search(re_pattern, target).group(1)
        # Content.token
        target = re.sub(re_pattern, str(getattr(Context, key)), target, 1)
    return target


if __name__ == '__main__':
    mystr = '{"member_id": "#member_id#", "loan_id": "#loan_id#", "token": "#token#", "username": "#username#"}'
    # print(replace_label(mystr))

    re_pattern = r'#(.*?)#'
    a = replace_label(mystr)
    print(a)









