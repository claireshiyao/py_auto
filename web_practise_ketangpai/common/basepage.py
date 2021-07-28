# author by claire
import datetime
import os
import time
from common import logger
from common.upload import upload
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import dir_config
import logging

class BasePage:
    def __init__(self, driver:WebDriver):
        self.driver = driver


    def wait_element_visible(self, loc, image_name, timeout=20, poll_frequency=0.5):
        logging.info("在{}开始等待{}元素可见".format(image_name, loc))
        # 开始等待前的当前时间
        time_before_wait = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency).until(EC.visibility_of_element_located(loc))
        except:
            self.save_page_shot(image_name)
            logging.exception("等待元素可见失败")
            raise
        else:
            # 结束等待的当前时间
            time_after_wait = datetime.datetime.now()
            wait_time = time_after_wait - time_before_wait
            logging.info("等待元素可见共用时：{}".format(wait_time))
    
    def wait_element_exists(self, loc, image_name, timeout=20, poll_frequency=0.5):
        logging.info("在{}开始等待{}元素存在".format(image_name, loc))
        # 开始等待前的当前时间
        time_before_wait = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency).until(EC.presence_of_element_located(loc))
        except:
            self.save_page_shot(image_name)
            logging.exception("等待元素存在失败")
            raise
        else:
            # 结束等待的当前时间
            time_after_wait = datetime.datetime.now()
            wait_time = time_after_wait - time_before_wait
            logging.info("等待元素存在共用时：{}".format(wait_time))

    def wait_element_clickable(self, loc, image_name, timeout=20, poll_frequency=0.5):
        logging.info("在{}开始等待{}元素可点击".format(image_name, loc))
        # 开始等待前的当前时间
        time_before_wait = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency).until(EC.element_to_be_clickable(loc))
        except:
            self.save_page_shot(image_name)
            logging.exception("等待元素可点击失败")
            raise
        else:
            # 结束等待的当前时间
            time_after_wait = datetime.datetime.now()
            wait_time = time_after_wait - time_before_wait
            logging.info("等待元素可点击共用时：{}".format(wait_time))

    def save_page_shot(self, image_name):
        # 当前时间
        cur_time = time.strftime("%Y-%m-%d %H_%M_%S")
        # 图片名称
        filename = "{}_{}.png".format(image_name, cur_time)
        # 截图存放路径
        file_path = os.path.join(dir_config.screenshots_path, filename)
        self.driver.save_screenshot(file_path)
        logging.info("截取当前网页图片成功，并保存在：{}".format(file_path))

    def get_element(self, loc, image_name):
        logging.info("在 {} 查找元素：{}.".format(image_name, loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.save_page_shot(image_name)
            logging.exception("定位元素失败")
            raise
        else:
            return ele

    def get_elements(self, loc, image_name):
        logging.info("在 {} 查找所有匹配到的元素：{}.".format(image_name, loc))
        try:
            ele = self.driver.find_elements(*loc)
        except:
            self.save_page_shot(image_name)
            logging.exception("定位元素失败")
            raise
        else:
            return ele

    def click_element(self, loc, image_name, timeout=20, poll_frequency=0.5):
        self.wait_element_visible(loc, image_name, timeout, poll_frequency)
        ele = self.get_element(loc, image_name)
        logging.info("在{}点击元素{}".format(image_name, loc))
        try:
            ele.click()
        except:
            self.save_page_shot(image_name)
            logging.exception("点击元素失败")
            raise

    def input_text(self, loc, text, image_name, timeout=20, poll_frequency=0.5):
        self.wait_element_visible(loc, image_name, timeout, poll_frequency)
        ele = self.get_element(loc, image_name)
        logging.info("在{}输入文本{}".format(image_name, text))
        try:
            ele.send_keys(text)
        except:
            self.save_page_shot(image_name)
            logging.exception("元素输入文本失败")
            raise

    def get_ele_attribute(self, loc, attr_name, image_name, timeout=20, poll_frequency=0.5):
        self.wait_element_visible(loc, image_name, timeout, poll_frequency)
        ele = self.get_element(loc, image_name)
        logging.info("在{}获取元素{}的{}属性".format(image_name, loc, attr_name))
        try:
            att_value = ele.get_attribute(attr_name)
        except:
            self.save_page_shot(image_name)
            logging.exception("获取元素属性失败")
            raise
        else:
            logging.info("属性值为：{}".format(att_value))
            return att_value

    def get_ele_text(self, loc, image_name, timeout=30, poll_frequency=0.5):
        self.wait_element_visible(loc, image_name, timeout, poll_frequency)
        ele = self.get_element(loc, image_name)
        logging.info("在{}获取元素{}的文本".format(image_name, loc))
        try:
            text = ele.text
        except:
            self.save_page_shot(image_name)
            logging.exception("获取元素文本失败")
            raise
        else:
            logging.info("文本为：{}".format(text))
            return text

    def switch_to_iframe(self, loc, image_name):
        """
        :param ref: 可以是元素，可以是下标数字，也可以是name属性
        :return:
        """
        logging.info("在{}等待iframe元素{}可用并切换到iframe".format(image_name, loc))
        try:
            WebDriverWait(self.driver,20).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except:
            self.save_page_shot(image_name)
            logging.exception("等待iframe可用失败")
            raise

    def switch_to_alert_and_accept(self, loc, image_name):
        logging.info("在{}等待alert元素{}存在并切换到alert".format(image_name, loc))
        try:
            WebDriverWait(self.driver, 20).until(EC.alert_is_present)
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            self.save_page_shot(image_name)
            logging.exception("等待alert存在失败")
            raise

    def switch_to_new_window(self, image_name):
        logging.info("准备切换到新窗口".format(image_name))
        time.sleep(2)
        wins = self.driver.window_handles
        try:
            self.driver.switch_to.window(wins[-1])
        except:
            self.save_page_shot(image_name)
            logging.exception("切换到新窗口失败")
            raise

    def execute_js_script(self, js, image_name, *args):
        try:
            self.driver.execute_script(js, *args)
        except:
            self.save_page_shot(image_name)
            logging.exception("js执行失败")
            raise


    def execute_script_date(self, loc, image_name, date, timeout=20, poll_frequency=0.5):
        self.wait_element_visible(loc, image_name, timeout, poll_frequency)
        ele = self.get_element(loc, image_name)
        logging.info("准备执行js修改日期值")
        try:
            self.driver.execute_script('var a = arguments[0]; a.readOnly=false; a.value=arguments[1]', ele, date)
        except:
            self.save_page_shot(image_name)
            logging.exception("修改日期值失败")
            raise

    def scroll_into_view(self, ele):
        self.driver.execute_script('arguments[0].scrollIntoView(false);', ele)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")

    def upload_file(self, filepath):
        upload(filepath)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.maximize_window()
    bp = BasePage(driver)
    bp.input_text(("id", "kw"), "web自动化", "百度页面_搜索输入操作", 5)
    bp.click_element(("id", "su"), "百度页面_点击百度一下")
    driver.quit()









