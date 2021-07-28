# author by claire

# 3.编写如下程序
#
# 假设一年的定期利率为3.52%，需要几年才能让定期存款连本带息的翻一番（例如：需要几年10000才能变成20000）

def profit(capital, interest_rate):
    sum = capital*(1 + interest_rate)
    return sum

if __name__ == '__main__':
    capital = float(input("本金:"))
    rate = float(input("利率:"))
    sum = profit(capital, rate)
    year = 1
    while True:
        if capital * 2 > sum:
            sum = profit(sum, rate)
        else:
            break
        year += 1
    print(f"需要{year}年本金翻番")
    print(sum)

# save_money = float(input("请输入你要存入银行的钱："))
#
# print("你存了{}元到银行!".format(save_money))
#
# TOTAL_MONEY = save_money * 2 # 定义变量用于保存总钱数
#
# year = 1 # 定义变量用于记录年份
#
# while save_money < TOTAL_MONEY:
#
#     save_money *= (1 + 0.0352)
#
#     year += 1
#
# print("定期利率为3.52%，需要{}年本金和才能翻一番。".format(year))
