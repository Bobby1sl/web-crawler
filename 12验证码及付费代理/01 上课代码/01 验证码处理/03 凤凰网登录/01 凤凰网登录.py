import base64
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import FENG_USERNAME, FENG_PASSWORD

driver = webdriver.Chrome()
driver.get('https://www.ifeng.com/')
driver.implicitly_wait(10)
driver.maximize_window()

"""点击右上角登录"""
driver.find_element(By.CSS_SELECTOR, '.login_in_2x-3NxtSKIw').click()
time.sleep(2)

"""切换进入到嵌套网页"""
iframe_label = driver.find_element(By.CSS_SELECTOR, '.box-1pZSPyeN>div>iframe')
driver.switch_to.frame(iframe_label)

"""点击消息提示框的账号登录"""
driver.find_element(By.CSS_SELECTOR, '.tab-2sXGklBv>span:nth-child(1)').click()
time.sleep(1)

"""输入用户名和密码"""
driver.find_element(By.CSS_SELECTOR, '.loginById-3HzkdnTl>div>div>input').send_keys(FENG_USERNAME)
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, '.input-2gdDY-Gz>div>input').send_keys(FENG_PASSWORD)
time.sleep(0.5)

"""保存图片验证码"""
# 获取验证码的标签对象
img_label = driver.find_element(By.CSS_SELECTOR, '.codeImg-2pONyHUT>img')
img_str = img_label.get_attribute('src')
print('src属性值:', img_str)
base64_str = img_str.split(',')[-1]
print('分割后的字符串图片数据: ', base64_str)

img_bayes = base64.b64decode(base64_str)  # 转化成二进制
with open('yzm.png', mode="wb") as f:
    f.write(img_bayes)
    print('验证码保存完成!!!')

"""调用打码平台识别验证码"""
from img_api import base64_api

result = base64_api('yzm.png', 7)
print('验证码识别结果:', result)

"""填入验证码"""
driver.find_element(By.CSS_SELECTOR, '.input-2N0ut5SW>div>input').send_keys(result)
time.sleep(2)

"""点击登录"""
driver.find_element(By.CSS_SELECTOR, '.submmitBtn-2AmMFR0C').click()

input()
driver.quit()
