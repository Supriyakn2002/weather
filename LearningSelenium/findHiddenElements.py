# SCENARIO-1 web element is there in the DOM but hidden.

"""from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import time

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

hidden_element = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
print(hidden_element)
time.sleep(3)
driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
time.sleep(3)
hidden_element1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
print(hidden_element1)
driver.quit()"""
# SCENARIO-2
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import time

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)

driver.get("https://hotel.yatra.com/nextui/hotel-search/dom/search?checkoutDate=09%2F03%2F2025&checkinDate=08%2F03%2F2025&source=BOOKING_ENGINE&pg=1&tenant=B2C&isPersnldSrp=1&city.name=Goa&city.code=Goa&state.name=Goa&state.code=Goa&country.name=India&country.code=IND&roomRequests%5B0%5D.id=1&roomRequests%5B0%5D.noOfAdults=2&roomRequests%5B0%5D.noOfChildren=0")

hidden_element = driver.find_element(By.ID, "body > main:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > nav:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3)").is_displayed()
print(hidden_element)
time.sleep(3)
driver.find_element(By.XPATH, "///nav[@id='EZDrawer__containerx0m1t']//div[contains(@class,'SelectRoom_selectorWrapper__OLC0A')]").click()
time.sleep(3)
hidden_element1 = driver.find_element(By.ID, "//label[@id='EZDrawer__overlayx0m1t']").is_displayed()
print(hidden_element1)
driver.quit()