# 1、总结类和对象的所有知识点。思维导图形式或者文字。


# 2、在之前定义的手机类下面定义智能手机类和苹果手机类。智能手机打电话可以具有录音功能。
# 苹果手机打电话不仅可以具有录音功能，还有 facetime 功能
class Phone:
    charge = True
    def call(self):
        print("可以打电话")
    def send_msg(self):
        print("可以发短信")

class SmartPhone(Phone):
    def __init__(self, model):
        self.model = model
    def record(self):
        print("{}正在电话录音".format(self))
    def __repr__(self):
        return self.model
    def call(self):
        super(SmartPhone, self).call()
        self.record()

class  IPhone(SmartPhone):
    def call(self):
        super().call()
        print("苹果手机不仅可以打电话录音")
    def facetime(self):
        print("还可以进行视频电话")

iphone = IPhone("iphone8")
iphone.call()
iphone.facetime()


# 3、定义一个 ExcelManual 类。具有获取 sheet 表单， 读取单元格 和 修改单元格功能。（不需要具体实现，只需要定义和传参。）
class ExcelManual:
    def __init__(self, name):
        self.name = name
    def get_sheet(self):
        print(f"{self.name}可以获取sheet表单")
    def read_cell(self):
        print(f"{self.name}可以读取单元格")
    def modify_cell(self):
        print(f"{self.name}可以修改单元格")
excelmanual = ExcelManual("excel工具")
excelmanual.get_sheet()
excelmanual.read_cell()
excelmanual.modify_cell()
