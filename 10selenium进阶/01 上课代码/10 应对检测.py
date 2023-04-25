from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 谷歌浏览器的配置项功能

driver = webdriver.Chrome()

# 一定要放在实例化浏览器下面
# 修改 window.navigator.webdriver 属性值
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})

driver.get('https://qikan.cqvip.com/Qikan/Journal/JournalGuid?from=index')
print(driver.page_source)

input()
driver.quit()
