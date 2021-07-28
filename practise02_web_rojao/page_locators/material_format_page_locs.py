# author by claire

from selenium.webdriver.common.by import By

class MaterialFormatPageLocs:
    # 素材格式链接
    meterial_format = (By.XPATH, '//a[@data-index="adv/advmaterialtype.html"]')
    # 素材格式iframe
    meterial_format_iframe = (By.XPATH, '//div[@id="iframe_adv_advmaterialtype_html"]//iframe[@class="tab_iframe"]')
    # 新增
    add_button = (By.XPATH, '//a[contains(text(),"新增")]')
    # 素材格式名称
    meterial_format_name = (By.XPATH, '//input[@name="materialTypeName"]')
    # 素材类型
    material_type = (By.XPATH, '//input[@name="picOrVideo" and @value="2"]')
    # 复选框
    check_box = (By.XPATH, '//input[@data-index="0" and @name="btSelectItem"]')
    # 新增确定
    add_confirm = (By.XPATH, '//input[@id="validateBtn"]')
    # 删除
    delete_button = (By.XPATH, '//a[@id="delete"]')
    # 提示语
    tip = [By.XPATH, '//div[@class="layui-layer-content"]']
    # 弹出框确定
    confirm_button = (By.XPATH, '//a[@class="layui-layer-btn0"]')

