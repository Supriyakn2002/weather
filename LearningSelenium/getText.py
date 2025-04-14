from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.edge.service import Service
service = Service(EdgeChromiumDriverManager().install())

driver = webdriver.Edge(service=service)

driver.get("https://www.yatra.com")

driver.implicitly_wait(10)

element = driver.find_element(By.XPATH, "//img[@alt='Top Destinations']")

alt_text = element.get_attribute("alt")

print("text:", alt_text)

driver.quit()


