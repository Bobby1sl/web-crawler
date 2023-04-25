from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 谷歌浏览器的配置项功能

# 声明一个谷歌配置对象
option = Options()

option.add_argument('--headless')  # 添加无头模式


driver = webdriver.Chrome(options=option)  # 在创建浏览器对象的时候使用配置项功能
driver.get('https://www.baidu.com/')
print(driver.page_source)



input()
driver.quit()

"""
    selenium的无头模式一般用于项目写完后添加, 因为写项目我们需要看到浏览器运行效果
    
    优点:
        1. 相对于有界面的浏览器运行更加快  -----原因在于您没有启动浏览器GUI，可以绕过真正的浏览器加载CSS、JavaScript、打开和呈现HTML所花费的所有时间。
"""
