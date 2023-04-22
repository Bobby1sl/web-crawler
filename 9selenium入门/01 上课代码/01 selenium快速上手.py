# pip install selenium

# 导入模块
from selenium import webdriver  # 浏览器功能


# 1. 实例化浏览器对象
driver = webdriver.Chrome()

# 2. 进行浏览器的自动化
driver.get('https://www.baidu.com/')


input()
# 3. 退出浏览器
driver.quit()


"""
selenium做的所有自动化的操作, 都是基于需求去操作的
咱们平常用户是怎么操作浏览器的, 那么咱们的代码和用户操作的顺序大致一致
浏览器页面的操作顺序, 就决定了代码顺序
"""