import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_product(keyword):
    """指定关键字搜索商品数据"""
    # # 找到搜索框, 输入关键字
    driver.find_element(By.CSS_SELECTOR, '#key').send_keys(keyword)
    time.sleep(1)
    # # 找到搜索按钮点击
    driver.find_element(By.CSS_SELECTOR, '.button').click()


def drop_down():
    """模拟人去滚动页面"""
    # input()
    time.sleep(1)
    for h in range(1, 10, 2):  # 13579  滚动5次
        j = h / 9  # 1/9  3/9  5/9  7/9  9/9
        js_all = f'document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}'
        driver.execute_script(js_all)
        time.sleep(0.5)  # 等待数据渲染

def parse_data():
    """解析数据函数"""
    lis = driver.find_elements(By.CSS_SELECTOR, '.gl-item')
    for li in lis:
        title = li.find_element(By.CSS_SELECTOR, 'div.p-name>a>em').text
        title = title.replace('京品电脑', '').replace('\n', '')

        price = li.find_element(By.CSS_SELECTOR, 'div.p-price>strong>i').text
        deal = li.find_element(By.CSS_SELECTOR, 'div.p-commit>strong>a').text
        store = li.find_element(By.CSS_SELECTOR, '.J_im_icon>a').text
        print(title, price, deal, store, sep=' | ')

        with open('jingdong.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([title, price, deal, store])


def get_next():
    """翻页函数"""
    driver.find_element(By.CSS_SELECTOR, '.pn-next>em').click()

if __name__ == '__main__':
    word = input('请输入您要搜索商品的关键字: ')
    driver = webdriver.Chrome()
    driver.get('https://www.jd.com/')
    driver.implicitly_wait(10)
    driver.maximize_window()

    # 调用搜索商品的函数
    get_product(word)

    for i in range(100):
        # 调用滚动页面的函数
        drop_down()
        # 调用数据解析函数
        parse_data()
        # 调用翻页函数
        get_next()

    input()
    driver.quit()