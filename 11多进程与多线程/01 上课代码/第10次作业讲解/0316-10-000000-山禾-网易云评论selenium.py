"""
目标网址:https://music.163.com/#/playlist?id=924680166

要求:
	1. 使用selenium
	2. 爬取前面5页的评论数据保存为txt文件
"""
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_data():
    """在页面中提取数据"""
    divs = driver.find_elements(By.CSS_SELECTOR, '.itm')

    for div in divs:
        contend = div.find_element(By.CSS_SELECTOR, '.cnt.f-brk').text
        contend = re.findall('：(.*)', contend)[0]
        print(contend)
        with open('contend.txt', mode='a', encoding='utf-8') as f:
            f.write(contend + '\n')




driver = webdriver.Chrome()
driver.get('https://music.163.com/#/playlist?id=924680166')

driver.switch_to.frame(0)
# print(driver.page_source)
# 下拉页面
js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
driver.execute_script(js)
# 使用selenium采集的数据我们要看的到

for i in range(5):
    parse_data()
    # 解析下一页标签点击
    driver.find_element(By.CSS_SELECTOR, '.znxt').click()
    time.sleep(2)

input()
driver.quit()

