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
driver.implicitly_wait(10)  # Wait up to 10 seconds before throwing an error

try:
    # Finding element by LINK_TEXT
    element = driver.find_element(By.LINK_TEXT, "Offers")
    print("Found element:", element.text)
except Exception as e:
    print("Error:", e)

driver.quit()
