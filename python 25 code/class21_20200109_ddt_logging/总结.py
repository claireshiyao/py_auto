"""
log 日志：
日志：记录。
代码当中：日志的作用是记录信息，便于我们查看问题，定位问题。

print()
logging: 标准库，

日志级别：
- 1、NOSET    0   等于没写，废话。
- 2，debug,  10,  调试，一些额外信息，备注，往往和主体功能无关。 日报里面的备注
- 3，info, 20  主体功能的信息。 日报，做了些啥？
- 4，warning, 30, 警告， 下次可能要出错了。 交警叔叔警告
- 5，error,  40,  犯错，违法。抢红灯
- 6, critical,  50, 极其严重。抢银行

如何定义级别：
1， 级别是我们自己定义的


"""
import logging

def old_function():
    try:
        1 / 0
        logging.info("代码没有问题")
    except Exception as e:
        # raise e
        logging.error(e)
    logging.warning("这个方法在下一个版本当中会被抛弃，如果正常使用，请用 new_function")
    return "hello"

def new_function():
    return "new"


a = 1
b = 2

c = a + b
# 记录 debug 信息
logging.info('知识一个普通的酱油信息')
logging.debug("这是一个 debug 信息")
logging.warning("这是一个警告信息")
logging.error('出错了，兄嘚')
logging.critical('奔溃了。')


if __name__ == '__main__':
    old_function()