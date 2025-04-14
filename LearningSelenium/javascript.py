from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Set up the WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.yatra.com/")
time.sleep(2)  # Wait for the page to load

# Locate the calendar input field (Replace with the correct selector for your site)
calendar_input = driver.find_element(By.ID, "datepicker")

# Scroll to the calendar input field
driver.execute_script("arguments[0].scrollIntoView();", calendar_input)

# Highlight the calendar input field
driver.execute_script("arguments[0].style.border='3px solid red'", calendar_input)

# Set the date using JavaScript
date_value = "2024-03-15"  # Adjust the format based on the site's expected input
driver.execute_script(f"arguments[0].value = '{date_value}';", calendar_input)

time.sleep(2)

# Take a screenshot
screenshot_path = "calendar_selection.png"
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved as {screenshot_path}")

print("Date selected successfully!")

# Close the browser

"""driver.execute_script("window.open('https://www.yatra.com/hotels','_self');")
demoElement = driver.execute_script("return document.getElementsByTagName('p')[5];")
driver.execute_script("arguments[0].click();",demoElement)
time.sleep(3)"""
driver.quit()
