import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 定位器功能


driver = webdriver.Chrome()
driver.get('https://www.jd.com/')

# 隐式等待, 是一种智能化等待, 虽然我设置了10秒等待时间, 但是如果在这个时间之前页面渲染完了, 那么不会死等
# 如果网站的连通性不好, 超过时间会报错
# 基于浏览器对象设置了一个隐式等待, 那么后续所有打开的页面都遵循这个规则
# driver.implicitly_wait(10)


time.sleep(5)  # 死等, 页面滚动等待页面渲染


input()
driver.quit()