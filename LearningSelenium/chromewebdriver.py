from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")

"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("C:\\BrowserDrivers\\chromedriver.exe"))
driver.get("https://www.google.com")
driver.maximize_window()
print(driver.title)
driver.close()"""

"""from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://selenium.dev")
driver.quit()"""


