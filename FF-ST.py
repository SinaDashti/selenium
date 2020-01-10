from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tabulate import tabulate
import pandas as pd

driver = webdriver.Firefox()
driver.get("https://www.speedtest.net")

# Waiting for banners and dismiss it
try:
    WebDriverWait(driver, 30).\
    until(EC.element_to_be_clickable\
    ((By.XPATH, "//*[@id='_evidon-banner-cookiebutton']"))).click()
    driver.find_element_by_xpath("//*[@id='_evidon-l3']/button").click()
except Exception as e:
    driver.get("https://www.speedtest.net")
    WebDriverWait(driver, 30).\
    until(EC.element_to_be_clickable\
    ((By.XPATH, "//*[@id='_evidon-banner-cookiebutton']"))).click()
    driver.find_element_by_xpath("//*[@id='_evidon-l3']/button").click()

# waiting for page to be loaded and shows the current server element
try:
    WebDriverWait(driver, 30).\
    until(EC.presence_of_element_located\
    ((By.XPATH, "//div[@data-view-name='currentServer']/div[2]/a")))
except Exception as e:
    print(e)

# start the test
driver.find_element_by_xpath("//*[@class='start-text']").click()

# wait for the test to be finished
try:
    WebDriverWait(driver, 120).until(EC.url_contains("result"))
except Exception as e:
    print(e)

# result extraction
result = driver.find_element_by_xpath(\
                "//div[@class='speedtest-container main-row']"\
                ).text.split('\n')

# print result
print(result)
c1 = result[10]
c2 = result[12]
c3 = result[14]
pi=[]
dl=[]
up=[]
pi.append(result[11])
dl.append(result[13])
up.append(result[15])
df = pd.DataFrame({c1:pi,c2:dl,c3:up})
df.index += 1
print(tabulate(df, headers='keys', tablefmt='psql'))

#  closing browser
driver.close()
