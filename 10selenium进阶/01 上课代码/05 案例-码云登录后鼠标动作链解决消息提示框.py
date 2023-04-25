import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://gitee.com/')
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, '.mb-0.contents>li:nth-child(2)>a').click()
driver.find_element(By.CSS_SELECTOR, '#user_login').send_keys('2535513449@qq.com')
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys('hjx_3136419')
time.sleep(2)
driver.find_element(By.NAME, 'commit').click()


# 页面跳转, 需要设置强制等待, 等待提示框渲染数据
time.sleep(2)
"""鼠标链坐标点击"""
# context_click 能够让我们看到坐标点的位置, 方便我们去定位
# ActionChains(driver).move_by_offset(1047, 350).context_click().perform()
ActionChains(driver).move_by_offset(1047, 350).click().perform()


input()
driver.quit()