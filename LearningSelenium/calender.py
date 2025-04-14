#//div[@aria-label='Choose Friday, April 11th, 2025']//span[contains(@class,'custom-day-content')][contains(text(),'₹5,255')]
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//div[@class='css-w7k25o']").click()
time.sleep(3)

click_date = driver.find_element(By.XPATH,"//span[normalize-space()='11']")
click_date.click()
time.sleep(2)
print("Date selected successfully!")

driver.quit()


