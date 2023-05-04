import base64
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from constants import BILIBILI_USERNAME, BILIBILI_PASSWORD

driver = webdriver.Chrome()
driver.get('https://passport.bilibili.com/login')
driver.implicitly_wait(10)
driver.maximize_window()

"""输入用户名和密码"""
driver.find_element(By.CSS_SELECTOR, '.tab__form>div:nth-child(1)>input').send_keys(BILIBILI_USERNAME)
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.tab__form>div:nth-child(3)>input').send_keys(BILIBILI_PASSWORD)
time.sleep(0.5)

"""点击登录"""
driver.find_element(By.CSS_SELECTOR, '.btn_wp>div:nth-child(2)').click()
# 点击登录后, 图片弹出需要设置强制等待
time.sleep(2)

"""保存图片"""
img_label = driver.find_element(By.CSS_SELECTOR, 'body>div:last-of-type div.geetest_holder')
img_label.screenshot('yzm.png')  # screenshot 直接根据标签对象截图
print('正在保存验证码....')

"""识别点选验证码"""
from img_api import base64_api

code_result = base64_api('yzm.png', 21)
print('验证码识别结果:', code_result)  # 122,222|42,242|250,194
split_result = code_result.split('|')  # ["122,222", "42,242", "250,194"]

for result in split_result:
    x = result.split(',')[0]  # x轴
    y = result.split(',')[1]  # y轴

    # move_to_element_with_offset  指定标签对象中的坐标点击
    ActionChains(driver).move_to_element_with_offset(img_label, int(x), int(y)).click().perform()
    time.sleep(1)

# pip install selenium==3.141.0  指定版本

time.sleep(5)
# 点击确认
driver.find_element(By.CSS_SELECTOR, 'body>div:last-of-type div.geetest_holder .geetest_commit_tip').click()

input()
driver.quit()
