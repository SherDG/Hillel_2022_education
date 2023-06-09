from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--no-sandbox")


# START DRIVER

driver = webdriver.Chrome(service=Service('/home/dima/Завантаження/Hillel/chromedriver'), options=options)
driver.maximize_window()

#get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
time.sleep(2)


# search the input tag which contains the 'id' attribute starts with 'search' text.
# driver. find_element(By.CSS_SELECTOR, "input[id^='search']").send_keys("Selenium")


# search the input tag which contains the 'id' attribute ending with 'strings' text.
# driver. find_element(By.CSS_SELECTOR, "input[id$='strings']").send_keys("Selenium")

# search the input tag which contains the 'id' attribute contains 'strings' text.
driver.find_element(By.CSS_SELECTOR, "input[id*='strings']").send_keys("Selenium")

time.sleep(2)

driver.close()
