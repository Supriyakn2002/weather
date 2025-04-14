from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Set up WebDriver using WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Google
driver.get("https://www.yatra.com/")
"""time.sleep(3)
driver.find_element(By.XPATH,"//p[@title='New Delhi']").click()
time.sleep(3)
departure = driver.find_element(By.XPATH,"//input[@id='input-with-icon-adornment']")
departure.click()
departure.send_keys("Bengaluru")
departure.send_keys(Keys.ENTER)
time.sleep(3)"""

arrival = driver.find_element(By.XPATH,"//p[@title='Mumbai']")
arrival.click()
going_to = driver.find_element(By.XPATH,"//input[@id='input-with-icon-adornment']")
going_to.send_keys("New")
"""search_results = driver.find_elements(By.XPATH,"//label[text()='Going To']//ancestor::div[3]//li")
print(len(search_results))
for results in search_results:
    if "new york" in results.text:
        results.click()
        time.sleep(5)
        break"""
driver.quit()

















"""# Find the search box and type a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium python")
time.sleep(2)  # Wait for autosuggestions to appear

# Get all autosuggestion elements
suggestions = driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li")

# Click on the second suggestion if available
if len(suggestions) > 1:
    suggestions[1].click()
else:
    print("No suggestions found")

# Wait to observe the result and close browser
time.sleep(5)
driver.quit()"""
