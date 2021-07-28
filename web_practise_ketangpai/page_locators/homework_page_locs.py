# author by claire

from selenium.webdriver.common.by import By


class HomeworkPageLocs:
    # 作业页面链接
    homework_page_link = (By.XPATH, '//a[text()="作业"]')
    # 作业链接
    homework_link = (By.XPATH, '//a[contains(text(), "20191126-自由发挥作业")]')
    # 更新提交按钮
    update_button = (By.XPATH, '//a[@class="new-tj1"]')
    # 更新提交弹框确定按钮
    update_confirm_button = (By.XPATH, '//a[text()="确定"]')
    # 添加作业按钮
    add_homework_button = (By.XPATH, '//a[@class="sc-btn webuploader-container"]')
    # 添加作业后提交按钮
    submit_button = (By.XPATH, '//div[@class="sc-tj fl"]')
    # 提交成功确定按钮
    submit_confirm_button = (By.XPATH, '//a[@class="weui_btn_dialog primary"]')
    # 作业状态按钮
    homework_status = (By.XPATH, '//a[@class="view-work"]')
    # 作业下载链接
    download_link = (By.XPATH, '//a[@class="download"]')
    # 留言块
    message_div = (By.XPATH, '//div[@id="mess1"]//following-sibling::div')
    # 留言输入框
    message_input = (By.XPATH, '//textarea[@id="comment"]')
    # 留言保存按钮
    message_save = (By.XPATH, '//a[text()="保存"]')



