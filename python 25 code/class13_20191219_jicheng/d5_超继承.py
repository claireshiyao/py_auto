class Phone:
    recharge = True

    def call(self):
        print("正在打电话")


class SmartPhone(Phone):

    def call(self):
        # 完全重写
        self.caputure_video()
        # # print("智能手机正在打电话")
        # super()
        # self.call()
        # super() 就是调用父类的 call() 方法。
        super().call()

    def caputure_video(self):
        print("正在视频")

smart = SmartPhone()
smart.call()