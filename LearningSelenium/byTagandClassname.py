from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open website
driver.get("https://www.yatra.com/")

# Wait for elements to load
driver.implicitly_wait(10)

# Find element by TAG NAME (Example: First <h1> tag)
tag_element = driver.find_element(By.TAG_NAME, "h1")
print("Found by Tag Name:", tag_element.text)

# Find element by CLASS NAME (Example: Replace 'your-class' with actual class)
class_element = driver.find_element(By.CLASS_NAME, "some-class")  # Change 'some-class' to the actual class name
print("Found by Class Name:", class_element.text)

driver.quit()
print(driver.page_source)
