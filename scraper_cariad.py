from selenium import webdriver
#from webdriver_manager.firefox import FirefoxDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def reject_cookies():
    cookies_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "onetrust-reject-all-handler"))
    )
    cookies_button.click()

def search(string):
    driver.find_element(By.ID, "jobSearchTextFilter").send_keys(string + Keys.ENTER)

def click_showMore():
    showMore_button = driver.find_element(By.ID, "showMoreButton")
    while showMore_button.is_displayed():
        showMore_button.click()
#        driver.implicitly_wait(5)


options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("https://cariad.technology/de/en/careers.html#joblist")

reject_cookies()
search("internship")
click_showMore()

time.sleep(10)
driver.quit()

t