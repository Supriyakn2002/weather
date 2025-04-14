"""from selenium import webdriver
from selenium.webdriver.edge.service import Service

edge_driver_path = "C:\\BrowserDrivers\\edgedriver_win64\\msedgedriver.exe"
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

driver.get("https://www.google.com")"""
from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://www.selenium.dev")
driver.maximize_window()
print(driver.title)
driver.close()
