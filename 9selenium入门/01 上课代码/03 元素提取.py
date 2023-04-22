import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 定位器功能


driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

"""
find_element    提取符合条件的第一个标签对象, 返回对象
find_elements   提取符合条件的所有标签对象, 返回列表
"""
"""数据标签对象提取"""
# 1. 根据标签的 id 值获取标签, 返回 <selenium.webdriver.remote.webelement.WebElement
result = driver.find_element(By.ID, 'anony-reg-new')
print(result)

# 2 根据标签的 name 属性值获取标签
result2 = driver.find_element(By.NAME, 'google-site-verification')
print(result2)

# 3 根据标签的 class 属性值获取标签
result3 = driver.find_element(By.CLASS_NAME, 'anony-nav-links')
print(result3)

# 4 根据标签包含的文本内容获取标签(精确匹配)
result4 = driver.find_element(By.LINK_TEXT, '下载豆瓣 App')
print(result4)

# 5 根据标签包含的文本内容获取标签(模糊匹配)
result5 = driver.find_elements(By.PARTIAL_LINK_TEXT, '豆瓣')
print(result5)
print(len(result5))

# 6. 根据标签的名字获取标签
result6 = driver.find_elements(By.TAG_NAME, 'div')
print(result6)
print(len(result6))

# 7 根据css选择器获取标签, 在selenium中css语法定位不支持属性提取器
result7 = driver.find_element(By.CSS_SELECTOR, '#anony-reg-new .app>a')
print(result7)
print('*' * 50)

# 8 根据xpath获取标签
result8 = driver.find_element(By.XPATH, '//*[@id="anony-reg-new"]//*[@class="app"]/a')
print(result8)

input()
driver.quit()