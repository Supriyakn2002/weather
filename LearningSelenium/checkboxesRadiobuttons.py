from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open webpage
driver.get("https://www.yatra.com/")
driver.maximize_window()
# Find the checkbox (Example: selecting the first checkbox on the page)
checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']").is_selected()
print(checkbox)
radio = driver.find_element(By.XPATH,"//input[@value='2']").is_selected()
print(radio)

# Click checkbox if it's not already selected
"""if not checkbox.is_selected():
    checkbox.click()

# Verify if checkbox is selected
print("Checkbox Selected:", checkbox.is_selected())

# Close the browser"""
driver.quit()
