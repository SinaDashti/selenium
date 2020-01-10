import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.speedtest.net")
try:
    element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='_evidon-banner-cookiebutton']"))
    )

    if element:
        driver.\
        find_element_by_xpath("//*[@id='_evidon-banner-cookiebutton']").click()
        driver.find_element_by_xpath("//*[@id='_evidon-l3']/button").click()
except Exception as e:
    print(e)
finally:
    driver.close()
