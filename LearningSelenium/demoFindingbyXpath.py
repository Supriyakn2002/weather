"""from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Or use webdriver.Firefox()

# Open a webpage
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

# Find elements using XPath
element = driver.find_element(By.XPATH, "//h1")  # Example: Finding an <h1> tag
print(element.text)  # Print the text inside the element

# Close the browser
driver.quit()"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

# Find element by XPath
element = driver.find_element(By.XPATH, "//input[@id='login-input']")

# Print element details
print("Element found:", element)

# Close browser
driver.quit()
