from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://practice.expandtesting.com/dropdown")

dd = driver.find_element(By.ID,"country")
multi = Select(dd)