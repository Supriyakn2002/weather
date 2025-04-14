from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Set up the WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
continuedemo = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
continuedemo.click()
time.sleep(2)
driver.save_screenshot(".\\test.png")
time.sleep(2)