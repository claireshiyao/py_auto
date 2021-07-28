"""
根据元素的特征，来确认元素的条件 ，然后根据条件去找到唯一的那个元素。

8大元素：

1、只根据元素的一个属性来找元素：6大
id
name
class_name - 只支持一个class值
tag_name

只针对a元素：
link_text
partial_link_text


2、多个属性组合来找元素或者通过其它的关系来找元素：2大

xpath - 语法  - F12下elements当中，按Ctrl +Ｆ　弹出表达式确认框
    绝对定位 - 以/开头， 父/子
    /html/body/div[2]/div[3]/div/div/div[2]/div[3]/i[1]   继承顺序、兄弟位置顺序
    //*[@id="number-attend"]/div[2]/div[3]/i[1]
    //div[@id="number-attend"]//i[@class="ing"]

    相对定位 - 靠自己的特征来定位  不在乎在第几代，不在乎是哪个小弟
    以//开头　－　有一个参照物
    1、//标签名[@属性=值]
    //i[@class="ing"]
    //*[@*="ing"]

    2、文本匹配   //标签名[text()=值]
    //a[text()="公告"]

    3、包含   //标签名[contains(@属性/text(),值)]
    //a[contains(@href,"/Notify/index/courseid/")]
    //a[contains(text(),"公告")]

    4、逻辑运算 来组合更多的元素特征。 and or
    //标签名[@属性=值 and @属性=值 and contains(@属性/text(),值) and text()=值]
    //标签名[@属性=值 or @属性=值]
    //a[text()="公告" and contains(@href,"/Notify/index/courseid/")]


　　5、层级定位：//一级元素//二级元素//......
       //div[@id="number-attend"]//i[@class="ing"]

   6、轴定位:  关系 - 分析元素之间的关系，页面的结构。
        1）通过兄弟姐妹找到自己
        2）通过后代元素来找到 祖先元素

        轴运算：
        ancestor：祖先结点 包括父
        parent:父结点   给g
        preceding: 当前元素节点标签之前的所有结点。（html页面先后顺序）
        preceding-sibling: 当前元素节点标签之前的所有兄弟结点
        following: 当前元素节点标签之后的所有结点。（html页面先后顺序）
        following-sibling：当前元素节点标签之后的所有兄弟结点

        使用语法：
        已知的元素/轴名称::标签名称[@属性=值]
        例：//div//table//td//preceding::td

        //p[@title="写忆"]/preceding-sibling::p[@class="stuno"]
        //p[@title="写忆"]/parent::*/following-sibling::li//p[@class="name"]


   7、下标/js

    # 说明页面 - 哪个元素
    # 元素定位表达式
    

css_selector - 晦se

"""

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# id
element = driver.find_element_by_id("kw")   # WebElement对象 - 1个对象对应1个元素
# driver.find_elements_by_id("kw")
element.send_keys("selenium webdriver")
driver.find_element_by_id('su').click()  # 带来了内容上的变化


# 1、输入操作  send_keys
# 2、点击操作  click
# 获取文本和获取属性

# # class - 只能是class属性当中的一个值
# driver.find_element_by_class_name("s_ipt")   # 1个元素 - 匹配到的第1个元素
# driver.find_elements_by_class_name("s_ipt")   # 所有匹配多个元素 - 列表
#
# # name
# driver.find_element_by_name("wd")
# driver.find_elements_by_name("wd")
#
# # tag
# driver.find_element_by_tag_name("input")
# driver.find_elements_by_tag_name("input")
#
# # link_text
# driver.find_element_by_link_text("地图")
# driver.find_elements_by_link_text("地图")
#
# # partial_link_text
# driver.find_element_by_partial_link_text("hao")
# driver.find_elements_by_partial_link_text("hao")

# driver.find_element_by_xpath('//p[@title="写忆"]/preceding-sibling::p[@class="stuno"]')

# # 直接写By,按Alt+Enter进行导入即可
# from selenium.webdriver.common.by import By
# # driver.find_element_by_css_selector('input#kw.s_ipt')
# element = driver.find_element(By.XPATH,'//p[@title="写忆"]/preceding-sibling::p[@class="stuno"]')
# element_list = driver.find_elements(By.XPATH,'//p[@title="写忆"]/preceding-sibling::p[@class="stuno"]')
#
