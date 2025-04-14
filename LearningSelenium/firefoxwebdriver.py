from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://selenium.dev")
driver.maximize_window()
print(driver.title)
driver.close()
