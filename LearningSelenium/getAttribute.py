from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

driver.get("https://www.yatra.com")

element = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")

attribute_value = element.get_attribute("class")

print("Attribute Value:", attribute_value)

driver.quit()
