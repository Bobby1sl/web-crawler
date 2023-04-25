
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 下拉框选项功能


driver = webdriver.Chrome()
driver.get('https://www.jq22.com/demo/shengshiliandong/')

# 找到有下拉框的<select>标签
element = driver.find_element(By.CSS_SELECTOR, '#s_province')


# 实例化 select 对象, 括号内部传递获取到下拉框标签对象
select = Select(element)

"""选择下拉框的方法"""
# # 根据索引取下拉框, 从1开始
select.select_by_index(1)  # 北京市
time.sleep(3)

# 根据下拉框的 value 取值
select.select_by_value('河北省')
time.sleep(3)

# 根据下拉框标签的文本取下拉框
select.select_by_visible_text('吉林省')




input()
driver.quit()

