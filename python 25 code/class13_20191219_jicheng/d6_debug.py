"""debug
调试，
1， 最简单的方式。 print()  缺陷：1，print(a),  2,调试完了还要删除
2, 出完问题，先 print() 百度。
3.  打断点。优先使用的调试

如果使用 debug 模式：
1， 小虫子的标记， 断点配合起来使用
2， 断点：程序运行到红点的地方，会暂停。

step over f8： 下一行， 单步调试
下一个断点:
运行到指定行：

step into: 进入对应的代码
step into my code:
"""

import time

class Phone:
    recharge = True

    def call(self):
        print("正在打电话")


class SmartPhone(Phone):

    def call(self):
        # 完全重写
        a = 4
        print(a)
        time.time()
        self.caputure_video()
        super().call()

    def caputure_video(self):
        c = 'hello'
        d = 'world'
        print("正在视频")

smart = SmartPhone()
print(smart)
smart.call()