from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a website with an iframe
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_height_width_css")
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH,""))

elem = driver.find_element(By.XPATH,"//h1[normalize-space()='This page is displayed in an iframe']")
elem.click()

driver.quit()


