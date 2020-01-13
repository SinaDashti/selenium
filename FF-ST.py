import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tabulate import tabulate
import pandas as pd
from bs4 import BeautifulSoup

pi = []
dl = []
up = []

driver = webdriver.Firefox()
driver.get("https://www.speedtest.net")

# Waiting for banners and dismiss it
try:
    WebDriverWait(driver, 30).\
    until(EC.element_to_be_clickable\
    ((By.XPATH, "//*[@id='_evidon-banner-cookiebutton']"))).click()
    driver.find_element_by_xpath("//*[@id='_evidon-l3']/button").click()
except Exception as e:
    try:
        WebDriverWait(driver, 30).\
        until(EC.element_to_be_clickable\
        ((By.XPATH, "//*[@id='_ev_opt_out_close']"))).click()
    except Exception as e:
        print(e)

# waiting for page to be loaded and shows the current server element
try:
    WebDriverWait(driver, 30).\
    until(EC.presence_of_element_located\
    ((By.XPATH, "//div[@data-view-name='currentServer']/div[2]/a")))
except Exception as e:
    raise

# start the test
driver.find_element_by_xpath("//*[@class='start-text']").click()

# wait for the test to be finished
try:
    WebDriverWait(driver, 120).until(EC.url_contains("result"))

# print(driver.current_url)
except Exception as e:
    print(e)

result = BeautifulSoup(driver.page_source, 'lxml')
sp = result.find_all('div', class_='result-container-data')[0]

c1 = 'PING ms'
c2 = 'DOWNLOAD Mbps'
c3 = 'UPLOAD Mbps'

pi.append(sp.find_all('div', class_='result-data u-align-left')[0].text.split('\n')[1])
dl.append(sp.find_all('div', class_='result-data u-align-left')[1].text.split('\n')[1])
up.append(sp.find_all('div', class_='result-data u-align-left')[2].text.split('\n')[1])

df = pd.DataFrame({c1:pi, c2:dl, c3:up})
df.index +=1
print(tabulate(df, headers='keys', tablefmt='psql'))
#
driver.close()
