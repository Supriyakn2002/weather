"""from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class demoFindElementbyID():
    def Locate_by_ID(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_id('login-input').send_keys('test@test.com')

findbyid = demoFindElementbyID()
findbyid.Locate_by_ID()"""

"""from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class demoFindElementByID():
    def Locate_by_ID(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        # Locate element by ID and enter email
        driver.find_element(By.ID, "login-input").send_keys("test@test.com")

findbyid = demoFindElementByID()
findbyid.Locate_by_ID()"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class DemoFindElementByID:
    def locate_by_ID(self):
        # Correct way to initialize WebDriver in Selenium 4
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        # Locate element by ID and enter email
        email_field = driver.find_element(By.ID, "login-input")
        email_field.send_keys("test@test.com")

        # Add a delay to observe the action
        import time
        time.sleep(5)

        driver.quit()  # Close browser after execution

# Run the script
findbyid = DemoFindElementByID()
findbyid.locate_by_ID()

