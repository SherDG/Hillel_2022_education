import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# First test - expected result -> word "Results" should be on the page

options = Options()
# options.add_argument("start-maximized"); # open Browser in maximized mode
# options.add_argument("disable-infobars"); # disabling infobars
# options.add_argument("--disable-extensions"); # disabling extensions
# options.add_argument("--disable-gpu"); # applicable to windows os only
# options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox")
# options.add_argument("headless")

# START DRIVER
driver = webdriver.Chrome(service=Service('/home/dima/Завантаження/Hillel/chromedriver'), options=options)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.python.org/")
# time.sleep(20) #sleep for 2 sec
# assert "Python_fail" in driver.title # Test fail
time.sleep(2) #sleep for 2 sec

# assert "Python" in driver.title

# find_element(By.TAG_NAME, "input")
# find_element(By.CLASS_NAME, "search-field")
# find_element(By.CSS_SELECTOR, "css selector")
elem = driver.find_element(By.ID, "id-search-field")

# elem = driver.find_element(By.NAME, "q")
# elem = driver.find_element(By.XPATH, '//*[@id="id-search-field"]')
elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
goButton = driver.find_element(By.ID, "submit")
goButton.click()


time.sleep(2) #sleep for 2 sec
# assert "No results found." not in driver.page_source
assert "Results" in driver.page_source
driver.close()