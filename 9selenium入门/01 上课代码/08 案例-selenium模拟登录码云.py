import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://gitee.com/')
driver.implicitly_wait(10)
driver.maximize_window()

"""点击登录按钮"""
driver.find_element(By.CSS_SELECTOR, '.mb-0.contents>li:nth-child(2)>a').click()

"""输入用户信息"""
driver.find_element(By.CSS_SELECTOR, '#user_login').send_keys('2535513449@qq.com')
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys('hjx_3136419')
time.sleep(2)

"""点击用户登录"""
driver.find_element(By.NAME, 'commit').click()


print(driver.get_cookies())  # 获取登录后的cookie

input()
driver.quit()