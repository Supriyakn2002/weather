#single select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.salesforce.com/in/form/signup/sales-ee/?d=topnav2-btn-ft")

driver.find_element(By.XPATH,"//input[@name='UserFirstName']").send_keys("abs")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='UserLastName']").send_keys("kn")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='UserTitle']").send_keys("eng")
time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
time.sleep(2)
dropdown = driver.find_element(By.XPATH,"//select[@name='CompanyEmployees']")
dd = Select(dropdown)
dd.select_by_index(1)
time.sleep(2)
dd.select_by_value("100")
time.sleep(2)
dd.select_by_visible_text("201 - 10,000 employees")
time.sleep(2)

dropdown1 = driver.find_element(By.XPATH,"//select[@name='CompanyCountry']")
dd1 = Select(dropdown1)
dd1.select_by_value("AR")
time.sleep(2)
dd1.select_by_visible_text("Belgium")
time.sleep(2)
"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open webpage
driver.get("https://www.salesforce.com/in/form/signup/sales-ee/?d=topnav2-btn-ft")

wait = WebDriverWait(driver, 10)

# Fill form fields (Using stable locators)
driver.find_element(By.XPATH, "//input[@name='UserFirstName']").send_keys("abs")
driver.find_element(By.XPATH, "//input[@name='UserLastName']").send_keys("kn")
driver.find_element(By.XPATH, "//input[@name='UserTitle']").send_keys("eng")

# Click the "Next" button after ensuring it's clickable
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next']")))
next_button.click()

# Wait for dropdown to load
dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[contains(@id, 'CompanyEmployees')]")))

# Handle dropdown selection
dd = Select(dropdown)
dd.select_by_visible_text("21 - 200 employees")

# Close browser after a short delay
import time
time.sleep(5)
driver.quit()"""
