from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains # 导入鼠标动作链功能


driver = webdriver.Chrome()

driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.switch_to.frame(0)

# 找到可以拖动的标签
drag = driver.find_element(By.CSS_SELECTOR, '#draggable')
# 找到放置的位置
drop = driver.find_element(By.CSS_SELECTOR, '#droppable')

"""鼠标动作链操作, 支持链式调用"""
# 实例化一个动作链对象, 括号内部需要传递当前driver浏览器对象
action = ActionChains(driver)

# 定义一个鼠标动作, 但是动作到目前为止还没有执行, 预编译
action.drag_and_drop(drag, drop)

# perform() 执行鼠标动作链
action.perform()


input()
driver.quit()
