"""
目标网址: https://github.com/login 模拟登录

作业要求:
    1.用 selenium 模拟登录GitHub(首先自己注册一个账号)
温馨提示:
    这个网站加载速度很慢, 最好设置时间长一点的等待
请在下方编写代码
"""
import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://github.com/login')
driver.implicitly_wait(10)
driver.maximize_window()

# 输入用户名
driver.find_element(By.CSS_SELECTOR, '#login_field').send_keys('hjx-edu')
time.sleep(2)

# 输入密码
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('qingdeng123')
time.sleep(2)

# 点击登录
driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-block.js-sign-in-button').click()


input()
driver.quit()




