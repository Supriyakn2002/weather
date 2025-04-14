from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a test webpage with JavaScript alerts
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()

"""# Click the button to trigger a JavaScript alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Switch to the alert and print its text
alert = driver.switch_to.alert
print("Alert Text:", alert.text)

# Accept the alert (Click OK)
alert.accept()
print("Alert accepted!")

# Click the button to trigger a confirmation alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert = driver.switch_to.alert
print("Confirm Alert Text:", alert.text)

# Dismiss the alert (Click Cancel)
alert.dismiss()
print("Alert dismissed!")

# Click the button to trigger a prompt alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alert = driver.switch_to.alert
print("Prompt Alert Text:", alert.text)

# Send text to the prompt alert and accept it
alert.send_keys("Hello, Selenium!")
alert.accept()
print("Prompt accepted with input!")

# Wait and close browser
time.sleep(2)
driver.quit()"""

driver.switch_to.frame("iframeResult")
#accept alert
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)"""

#dismiss alert
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)

"""#send text
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(2)
driver.switch_to.alert.send_keys("sup")
driver.switch_to.alert.accept()
time.sleep(2)"""

