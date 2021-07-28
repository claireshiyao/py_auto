"""
- 1， 日志收集器 logger:  日记本
- 2， 日志收集器级别 level
- 3， 日志处理器准备 handler， 不同记号的笔
- 4， 日志处理器级别设置
- 5, logger.addHandler(hadler)
- 6， 设置日志格式  format，   日期：重要程度：分类（工作，生活）：内容 fmt = logging.Format()
- 7， 添加日志处理器, handler.setFormat()

设置级别：
当设成 debug 的时候，只有 高于，等于改级别的才会打印。
当你成成  warning, 只有 warning， error， critical

"""
import logging

# 初始化 logger 收集器
logger = logging.getLogger('python25')

# 设置级别

logger.setLevel('DEBUG')

# 笔的默认级别是warning, 默认是使用控制台输出。
# 放到一个file 文件当中
handler =  logging.FileHandler('log.txt')
console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

handler.setLevel('WARNING')
# 添加 handler
logger.addHandler(handler)
logger.addHandler(console_handler)

# handler 设置格式
fmt  =  logging.Formatter('%(filename)s-%(lineno)d - %(name)s-%(levelname)s-%(message)s')
handler.setFormatter(fmt)

logger.info('hello')
logger.warning('world')
