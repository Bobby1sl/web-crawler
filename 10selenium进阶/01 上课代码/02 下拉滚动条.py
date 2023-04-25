from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.douban.com/')

# document.documentElement.scrollTop  指定滚动条的位置
# document.documentElement.scrollHeight  获取当前页面的最大高度
js = 'document.documentElement.scrollTop=2000'
js_all = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'

# 有些时候页面的高度会不断地改变, 需要给一定的时间去让浏览器去渲染数据

driver.execute_script(js_all)


input()
driver.quit()
