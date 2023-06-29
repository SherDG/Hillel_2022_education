from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service('/home/dima/Завантаження/Hillel/chromedriver'), options=options)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")
# driver.get("https://qauto2.forstudy.space/")

time.sleep(3)  # sleep for 3 sec

driver.close()
