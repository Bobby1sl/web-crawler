# 在百度搜索框输入  python ，全选,复制,剪切,粘贴 跳转到搜狗输入框进行搜索

import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys  # 键盘事件功能


driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

input_label = driver.find_element(By.CSS_SELECTOR, '#kw')
input_label.send_keys('python')
time.sleep(3)

input_label.send_keys(Keys.CONTROL, 'a')  # 全选
time.sleep(3)

input_label.send_keys(Keys.CONTROL, 'c')  # 复制
time.sleep(3)

input_label.send_keys(Keys.CONTROL, 'x')  # 剪切
time.sleep(3)


driver.get('https://www.sogou.com')
sougou_input = driver.find_element(By.CSS_SELECTOR, '#query')
sougou_input.send_keys(Keys.CONTROL, 'v')
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#stb').send_keys(Keys.ENTER)


input()
driver.quit()

# 键盘事件要基于标签对象操作, 没有对象无法直接操作键盘事件