import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 定位器功能


driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
time.sleep(3)

driver.get('https://news.baidu.com/')
time.sleep(3)

driver.back()  # 后退到上一级页面
time.sleep(3)
print(driver.page_source)


driver.forward()  # 前进到下一个页面
time.sleep(3)
print(driver.page_source)

# driver.refresh()  # 页面刷新, 在一个网页中如果后退, 会导致旧页面元素不可用, 那么要刷新一下

input()
driver.quit()