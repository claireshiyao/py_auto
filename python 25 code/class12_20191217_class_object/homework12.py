# 1.编写如下程序
# 编写一个数学计算类，要求初始化方法带参数（传两个数字），能够实现加减乘除运算（方法）。
class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        c = self.a + self.b
        return c
    def sub(self):
        c = self.a - self.b
        return c
    def multiply(self):
        c = self.a * self.b
        return c
    def divide(self):
        c = self.a / self.b
        return c
res = Calculation(4, 1)
print("加法结果", res.add())
print("减法结果", res.sub())
print("乘法结果", res.multiply())
print("除法结果", res.divide())

"""
2、实现文字版游戏：坦克大战 （非继承版）

1、电脑坦克和玩家坦克会有以下属性或者方法：
拥有live属性（这个属性代表Tank是否存活 :  1代表活的，0代表死）
拥有postion属性（这个属性代表Tank的位置，位置随机生成，一共有（1,10）10个位置）
拥有HP属性（代表血量，默认为10）
拥有attck_postion属性（代表攻击位置，位置随机生成，一共有（1,10）10个位置）
BeseTank拥有HP属性（代表血量，默认为10）
拥有一个hit方法，该方法除self外，还接收一个参数other(代表对方Tank)，在该方法中判断，对方攻击位置和自己所在的位置是否一致，如果一致的话，就给自己的HP减1，当HP等于0时，修改live属性（改为死亡状态）
2、实现一个玩家坦克类，该类还拥有两个方法。
move方法：(移动tank位置)调用该方法时，提示玩家输入移动的目标位置，输入完之后，将坦克移动到输入的位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
Bullet_launch方法：发射子弹，提示玩家输入攻击的目标位置，（输入无效数据，提示用户重新输入，通过异常来处理无效数据）
3、实现一个电脑坦克类，该类还拥有两个方法。
move方法：(移动tank位置) 调用该方法时，随机移动位置（1,10）
Bullet_launch方法：发射子弹，攻击目标位置随机生成（1,10），
"""



# 3， 定义一个手机类， 具有打电话和录音的功能，打电话的时候可以录音，也可以不录音。
class MobilePhone:
    def __init__(self, name):
        self.name = name

    def call(self, recording):
        print('我用的是{}'.format(self.name))
        print("可以打电话")
        if recording == 'yes':
            self.record(self)
            return "打电话的同时可以进行录音"
        elif recording == 'no':
            return "打电话的时候可以不录音"

    @staticmethod
    def record(self):
        print("可以进行录音")

phone = MobilePhone('华为手机')
print(phone.call("yes"))


# 二、选作题（不需要提交)
# 1.编写如下程序
# 编写一个工具箱类和工具类，需要有工具的名称、功能描述、价格，能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
tools = ["文件夹", "文件架", "文件袋", "订书机"]
class ToolKit:
    def __init__(self, name):
        self.toolkit_name = name
    def add_tools(self, tool):
        tools.append(tool)
        return f"添加{tool}工具后, 现有工具有：{tools} "
    def remove_tools(self, tool):
        tools.remove(tool)
        return f"删除{tool}工具后, 现有工具有：{tools} "
    def check_tools(self):
        return f"现有工具有：{tools}"
    def check_tool_number(self):
        num = len(tools)
        return "现有工具总数:{}".format(num)
file_toolkit = ToolKit("办公用品工具箱")
print(file_toolkit.add_tools("剪刀"))
print(file_toolkit.check_tool_number())
print(file_toolkit.check_tools())

class Tools:
    def __init__(self, name, price):
        self.tool_name = name
        self.price = price
    @ staticmethod
    def collect_files(self):
        return '可以收纳整理文件'
folder = Tools("文件夹", "1元")
file_packet = Tools("文件袋", "3元")
print(folder.tool_name, folder.collect_files('self'))

