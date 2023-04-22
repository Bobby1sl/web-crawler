import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 定位器功能


driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

"""
text 属性
    可以根据标签对象提取包含的文本内容, 支持链式调用
"""
# result = driver.find_element(By.XPATH, '//*[@id="anony-reg-new"]//*[@class="app"]/a')
# print(result)
# print(result.text)

result = driver.find_element(By.XPATH, '//*[@id="anony-reg-new"]//*[@class="app"]/a').text
print(result)

"""
get_attribute('href')
    方法.  根据标签对象的属性名, 提取其属性值, 支持链式调用
"""
result = driver.find_element(By.XPATH, '//*[@id="anony-reg-new"]//*[@class="app"]/a').get_attribute('href')
print(result)

"""
send_keys('流浪地球2')
    基于获取到的标签对象输入数据, 必须这个标签对象要有输入框
"""
driver.find_element(By.CSS_SELECTOR, '.inp>input').send_keys('流浪地球2')

"""
.click()      执行标签对象的点击操作, 需要该标签对象具有点击事件
"""
driver.find_element(By.CSS_SELECTOR, '.bn>input').click()

input()
driver.quit()