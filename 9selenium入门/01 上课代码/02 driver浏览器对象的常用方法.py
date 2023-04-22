import time

from selenium import webdriver


driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')

# save_screenshot()  制定路径对浏览器页面截屏
driver.save_screenshot('百度.png')

# page_source 查看当前浏览器渲染后的数据
# 这个数据有可能和真实的浏览器得到的数据会不一样
print(driver.page_source)

# with open('a.html', mode='w', encoding='utf-8') as f:
#     f.write(driver.page_source)

# get_cookies() 获取页面请求后的 cookie
# 用selenium模拟登录, 可以获取到用户登录后的cookies, 这个cookies也可以对接到 requests
print(driver.get_cookies())

# 查看当前页面的url地址
print(driver.current_url)

# 最大化浏览器
driver.maximize_window()

time.sleep(3)

# 最小化浏览器
driver.minimize_window()

input()

# 退出整个浏览器
driver.quit()