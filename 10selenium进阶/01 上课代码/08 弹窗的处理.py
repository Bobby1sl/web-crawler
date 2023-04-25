from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains # 导入鼠标动作链功能


driver = webdriver.Chrome()

driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.switch_to.frame(0)
drag = driver.find_element(By.CSS_SELECTOR, '#draggable')
drop = driver.find_element(By.CSS_SELECTOR, '#droppable')
action = ActionChains(driver)
action.drag_and_drop(drag, drop)
action.perform()

"""处理弹窗"""
alert = driver.switch_to.alert  # 切换到弹窗
print(alert.text)

alert.accept()  # 点击弹窗中的确认




input()
driver.quit()
