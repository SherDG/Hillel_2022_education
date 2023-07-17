import pytest

from POM.pages.homepage import Homepage
# from POM.pages.garage import Garage
from POM.pages.sign_in_page import SignInPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("start-maximized"); # open Browser in maximized mode
options.add_argument("--no-sandbox")
# options.add_argument("headless")

# @pytest.fixture()
# def set_up_driver():
#     # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     driver = webdriver.Chrome(service=Service('/home/dima/Завантаження/Hillel/chromedriver'), options=options)
#     driver.get("https://bstackdemo.com/")
#     yield driver
#     driver.quit()


def test_browserstack():
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver = webdriver.Chrome(service=Service('/home/dima/Завантаження/Hillel/chromedriver'), options=options)
    driver.get("https://bstackdemo.com/")
    # driver = set_up_driver
    homepage = Homepage(driver)
    # garage = Garage(driver)
    sign_in_page = SignInPage(driver)

    homepage.click_sign_in()

    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()

    # assert "demouser"  in driver.page_source
    homepage.check_username()
    driver.quit()