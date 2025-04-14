"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev")
print(driver.title)
driver.close()"""

# selenium 4
"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
driver.get("https://www.selenium.dev")
print(driver.title)
driver.close()"""

"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("user-agent=Brave")  # Make Chrome behave like Brave

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType  # Correct import

# Set up options for Brave
options = Options()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"  # Update if needed

# Install and use Brave driver
service = Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
driver = webdriver.Chrome(service=service, options=options)

# Open website and print title
driver.get("https://www.selenium.dev")
print(driver.title)

# Close browser
driver.quit()

