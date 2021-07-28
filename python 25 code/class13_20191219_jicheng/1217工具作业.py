#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/6/18 15:08

class Tool:
    """
    定义工具类
    """

    def __init__(self, name, desc, price):
        """
        构造方法
        :param name: 工具名称
        :param desc: 工具描述
        :param price: 工具价格
        :return: 无
        """
        self.name, self.desc, self.price = name, desc, price

    def describe_tool(self):
        """
        获取工具描述信息
        :return:
        """
        print("\n{:*^100}".format("开始描述"))
        print("名称：{0.name}\n功能：{0.desc}\n价格：{0.price}".format(self))
        print("{:*^100}\n".format("结束描述"))
        # print("描述工具\n名称：{}\n功能：{}\n价格：{}".format(self.name, self.desc, self.price))

    def __str__(self):
        return "<{}>".format(self.name)


class ToolPackage:
    """
    定义工具箱类
    """
    tools_count = 0

    # tools 不作为参数传入，也可以作为参数传入
    def __init__(self, name):
        self.name = name
        self.all_tools = []  # 存放工具的列表

    def add(self, one_tool):
        """
        添加工具到工具箱中
        :param one_tool: Tool工具对象
        :return:
        """
        if isinstance(one_tool, Tool):
            self.all_tools.append(one_tool)
            self.modify_tool_count()
            print("成功添加【{}】到【{}】中！".format(one_tool.name, self.name))
        else:
            print("{}不是工具对象，无法添加！".format(one_tool))

    def has_tool(self, one_tool):
        """
        判断工具是否在工具箱中
        :param one_tool: Tool工具对象或者工具名
        :return: True or False
        """
        if isinstance(one_tool, Tool):  # 如果one_tool是工具对象
            return one_tool in self.all_tools  # 判断是否在工具箱中
        elif isinstance(one_tool, str):  # 如果是工具名，字符串
            for tool_obj in self.all_tools:
                if one_tool == tool_obj.name:
                    return True
        return False

    def remove(self, one_tool):
        """
        删除工具
        :param one_tool: Tool工具对象或者工具名称
        :return:
        """
        if self.has_tool(one_tool):  # 如果要删除的工具存在
            if isinstance(one_tool, Tool):  # 如果one_tool为Tool工具对象
                self.all_tools.remove(one_tool)
            else:  # 为工具名称字符串

                for index, item in enumerate(self.all_tools):
                    if one_tool == item.name:  # 当前遍历的工具名为one_tool
                        self.all_tools.pop(index)
                        break  # 删除之后，退出循环
        else:
            print("工具不存在，无法删除！")

    def search(self, one_tool):
        """
        根据工具对象或者工具名称查找工具
        :param one_tool: Tool工具对象或者工具名称
        :return:
        """
        if self.has_tool(one_tool):
            if isinstance(one_tool, Tool):  # 如果one_tool为Tool工具对象
                one_tool.describe_tool()
            else:  # 为工具名称字符串
                for index, item in enumerate(self.all_tools):
                    if one_tool == item.name:  # 当前遍历的工具名为one_tool
                        self.all_tools[index].describe_tool()
                        break  # 找到工具之后，退出循环
        else:
            print("工具不存在！")

    @classmethod
    def modify_tool_count(cls):
        """
        类方法，每调用一次工具总数加一
        :return:
        """
        cls.tools_count += 1

    @classmethod
    def get_tool_count(cls):
        """
        类方法，获取工具箱中，工具总数
        :return:
        """
        return cls.tools_count


hammer = Tool("锤子", "由金属或木头等材料做成的头和与之垂直的柄构成的敲击工具。", 25.2)
# screwdriver = Tool("螺丝刀", "是一种用来拧转螺丝以使其就位的工具，通常有一个薄楔形头，可插入螺丝钉头的槽缝或凹口内。", 5)
# saw = Tool("锯子", "用来把木料或者其他需要加工的物品锯断或锯割开的工具。", 12)
# electric_drill = Tool("电钻", "利用电做动力的钻孔机具。", 278)

family_tool_package = ToolPackage("家用工具箱")
# 将工具添加到工具箱中
family_tool_package.add(hammer)

family_tool_package.remove('锤子')

print(family_tool_package.all_tools)
