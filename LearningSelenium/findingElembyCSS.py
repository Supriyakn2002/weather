from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

# Find element by CSS selector (Example: Email input field)
element = driver.find_element(By.CSS_SELECTOR, "input#login-input")

# Print element details
print("Element found:", element)

# Close browser
driver.quit()
