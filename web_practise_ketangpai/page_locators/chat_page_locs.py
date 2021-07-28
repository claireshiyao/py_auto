# author by claire
from selenium.webdriver.common.by import By


class ChatPageLocs():
    # 联系人按钮
    contact_button = (By.XPATH, '//a[text()="联系人"]')
    # contact_button = (By.XPATH, '//div[@class="totalbar"]//a[text()="联系人"]')
    # web实战项目班级下拉列表
    web_practise_list = (By.XPATH, '//h2[@title="python-web项目实战- 考核项目"]')
    # web实战项目班级小简头像
    Xiaojian_avatar = (By.XPATH, '//h2[@title="python-web项目实战- 考核项目"]//following-sibling::ul//p[text()="小简"]')
    # 聊天文本输入框
    text_input = (By.XPATH, '//textarea[@class="ps-container"]')
    # 附件
    attachment_button = (By.XPATH, '//a[@id="upload"]')
    # 发送按钮
    send_button = (By.XPATH, '//a[text()="发送"]')
    # 聊天框消息内容
    # message_text = (By.XPATH, '//div[@class="self"]//div[@class="text"]')
    message_text = (By.XPATH, '//div[@class="text"]')
    # 聊天框文件下载链接
    download_link = (By.XPATH, '//a[@class="download"]')
    # 搜索框
    search_input = (By.XPATH, '//div[@class="search-box"]//input[@type="text"]')
    # 搜索列表web实战项目班级小简头像
    search_xiaojian_avatar = (By.XPATH, '//span[@title="python-web项目实战- 考核项目"]//parent::dt//following-sibling::dd//span[@title="小简"]')
    # 搜索框关闭按钮
    close_search_button = (By.XPATH, '//a[@class="close"]')
    # 最近消息按钮
    lately_button = (By.XPATH, '//a[text()="最近"]')
    # 最近消息小简头像
    lately_message_xiaojian_avatar = (By.XPATH, '//div[@class="m-list"]//p[text()="小简"]')
    # 发送错误提示语
    error_tip =(By.XPATH, '//div[@id="error-tip"]//span')