import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.speedtest.net")

# Waiting for banners and dismiss it
try:
    WebDriverWait(driver, 30).\
    until(EC.element_to_be_clickable\
    ((By.XPATH, "//*[@id='_evidon-banner-cookiebutton']"))).click()
    driver.find_element_by_xpath("//*[@id='_evidon-l3']/button").click()
except Exception as e:
    print(e)

# waiting for page to be loaded and shows the current server element
try:
    WebDriverWait(driver, 30).\
    until(EC.presence_of_element_located\
    ((By.XPATH, "//div[@data-view-name='currentServer']/div[2]/a")))
except Exception as e:
    raise

driver.close()
