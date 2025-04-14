from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service  = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(3)

parent_handle = driver.current_window_handle #there's a unique id or window handles for each window
time.sleep(2)
print(parent_handle)

time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='AXISRUPAY']").click()
all_handles = driver.window_handles
print(all_handles)

for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[@id='booking_engine_luxury_trains']").click()
        time.sleep(2)
        driver.close()
        time.sleep(2)
        break
driver.switch_to.window(parent_handle)
driver.find_element(By.XPATH,"//span[normalize-space()='AXISRUPAY']").click()

driver.quit()