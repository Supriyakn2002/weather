from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import time

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

driver.get("https://demo.owasp-juice.shop/#/login")

element = driver.find_element(By.XPATH, "//button[@id='loginButton']//span[@class='mat-button-wrapper']")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc@abc")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("abc@123")
time.sleep(3)
if element.is_enabled():
    print("Element is enabled")
else:
    print("Element is disabled")

driver.quit()
