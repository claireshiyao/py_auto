#  -*-coding:utf8 -*-

success = {'money': 1000}
invalid_invest_money = [{'money': -10, 'check': '请正确填写投标金额'},
                        {'money': 0, 'check': '请正确填写投标金额'},
                        {'money': ' ', 'check': '请正确填写投标金额'},
                        {'money': 30, 'check': '投标金额必须为100的倍数'}
                        ]
