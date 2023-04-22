import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 定位器功能


driver = webdriver.Chrome()
driver.get('https://www.douban.com/')

# 点击豆瓣读书
driver.find_element(By.CSS_SELECTOR, '.anony-nav-links>ul>li:nth-child(1)').click()

# driver.window_handles 获取当前浏览器所有的页面窗口
print(driver.window_handles)

time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

driver.close()  # 关闭当前窗口, 如果当前只有一个窗口, 那么就会退出浏览器

input()
driver.quit()