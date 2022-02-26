from selenium import webdriver
#from webdriver_manager.firefox import FirefoxDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def click_advanced_search():
    driver.find_element(By.CLASS_NAME, "btn-inline-alt btn-inline--svg form-search__advance-button").click()


def click_buy():
    driver.find_element(By.CLASS_NAME, "btn-inline-alt btn-inline--svg form-search__advance-button").send_keys(string + Keys.ENTER)


def click_showMore():
    showMore_button = driver.find_element(By.ID, "showMoreButton")
    while showMore_button.is_displayed():
        showMore_button.click()
#        driver.implicitly_wait(5)


options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://www.aspc.co.uk")





reject_cookies()
search("internship")
click_showMore()

time.sleep(10)
driver.quit()

