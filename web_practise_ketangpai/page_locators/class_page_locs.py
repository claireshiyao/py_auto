# author by claire
from selenium.webdriver.common.by import By


class ClassPageLocs:
    # 加入课程
    join_class_link = (By.XPATH, '//div[@class="ktcon1l fr"]')
    # 加课验证码输入框
    class_captcha_input = (By.XPATH, '//div[@class="chuangjiankccon"]//input')
    # 加入按钮
    join_button = (By.XPATH, '//li[@class="cjli2"]//a')
    # 加课成功提示语
    join_success_tip = (By.XPATH, '//div[@id="show-tip"]//span')
    # 加课验证码错误提示语
    join_error_tip = (By.XPATH, '//div[@id="error-tip"]//span')
    # web项目实战
    class_name_link = (By.XPATH, '//dt[@class="bgclass1"]//a[@title="python-web项目实战- 考核项目"]')
    # 柠檬班-考核项目的更多选项
    select_more_link = (By.XPATH, '//dt[@class="bgclass1"]//a[@class="kdmore"]')
    # 退课
    drop_class_link = (By.XPATH, '//dt[@class="bgclass1"]//a[text()="退课"]')
    # 退课成功提示语
    drop_success_tip = (By.XPATH, '//div[@id="show-tip"]//span')
    # 登录密码验证输入框
    login_password_input = (By.XPATH, '//div[@class="deletekccon"]//input')
    # 退课确认按钮
    drop_class_confirm_button = (By.XPATH, '//div[@class="deletebot cl"]//a[@class="btn btn-positive"]')
    # 退课取消按钮
    drop_class_cancel_button = (By.XPATH, '//div[@class="deletebot cl"]//a[@class="btn btn-default"]')
    # 成绩
    grade_link = (By.XPATH, '//a[text()="成绩"]')
    # 登录验证码错误提示语
    login_password_error_tip = (By.XPATH, '//div[@id="error-tip"]//span')
    # 私信按钮
    chat_button = (By.XPATH, '//a[@href="/Letter/index.html"]')








