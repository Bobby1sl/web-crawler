from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://music.163.com/#/song?id=1450083773')


# 默认情况下selenium是无法获取到嵌套网页数据

"""切换进入到嵌套网页"""
# 方式一: 根据索引切换进入到嵌套网页
"""
switch_to.frame() 切换嵌套网页
frame(0)  根据嵌套网页的索引切换进入
如果索引超过嵌套网页已有的数量, 就会报错 ---> selenium.common.exceptions.NoSuchFrameException: Message: no such frame
"""
# driver.switch_to.frame(10)


# 方式二: 根据嵌套网页的<iframe>对象, 切换进入到嵌套网页
iframe = driver.find_element(By.CSS_SELECTOR, '#g_iframe')
driver.switch_to.frame(iframe)


# 退出嵌套网页
driver.switch_to.parent_frame()  # 从嵌套网页, 切换到父级网页
# 如果嵌套网页的结构是2层以上, 要一级一级退出

print(driver.page_source)

input()
driver.quit()
