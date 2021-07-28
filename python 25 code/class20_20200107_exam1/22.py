# author by claire

# 2.编写如下程序
#
# 用户输入考试成绩，当分数高于90（包含90）时打印A；否则如果分数高于80（包含80）时打印B；
# 否则如果当分数高于70（包含）时打印C；否则如果当分数高于60（包含60）时打印D；其他情况就打印E


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"

if __name__ == '__main__':
    try:
        score = float(input("成绩："))
        print(grade(score))
    except Exception as e:
        print("请输入数字")