import random
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get('https://www.wjx.cn/jq/87910206.aspx')

divs = driver.find_elements(By.CSS_SELECTOR, '.div_question')
print(divs)
print(len(divs))

"""
单选  索引->0-9
多选  索引->10-11
"""
one_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
any_choice = [10, 11]


"""解决单选"""
for i in one_choice:
    lis = divs[i].find_elements(By.CSS_SELECTOR, 'ul>li')  # 获取每一个题目下的选项
    random.choice(lis).click()  # 随机选择一个选项点击

"""解决多选"""
for j in any_choice:
    lis = divs[j].find_elements(By.CSS_SELECTOR, 'ul>li')  # 获取每一个题目下的选项
    # random.choices()  # 可能会重复
    lis_ = random.sample(lis, k=3)  # 随机选多个不重复的
    for l in lis_:
        l.click()

# 点击提交
driver.find_element(By.CSS_SELECTOR, '#submit_button').click()
time.sleep(1)

# 点击智能认证
driver.find_element(By.CSS_SELECTOR, '.sm-ico .sm-ico-wave').click()

input()
driver.quit()
