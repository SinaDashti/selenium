from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tabulate import tabulate
import pandas as pd
from bs4 import BeautifulSoup
import sys

pi = []
dl = []
up = []
server = []
link = []
ser_link = {}

for rep in range(0, int(sys.argv[1])):
    driver = webdriver.Firefox()
    driver.get("https://www.speedtest.net")

    # Waiting for banners and dismiss it
    try:
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='_evidon-banner-cookiebutton']"))).click()
        driver.find_element_by_xpath("//*[@id='_evidon-l3']/button").click()
    except Exception as e:
        try:
            WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='_ev_opt_out_close']"))).click()
        except Exception as e:
            print(e)

    # waiting for page to be loaded and shows the current server element
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@data-view-name='currentServer']/div[2]/a")))
    except Exception as e:
        raise

    # choosing server
    driver.find_element_by_xpath(
        "//div[@class='result-data'][2]/child::a[1]").click()

    li = driver.find_elements_by_xpath(
        "//ul[@data-view-name='serverCollection']/li")

    for x in range(1, (len(li) + 1)):

        p1 = "//ul[@data-view-name='serverCollection']/li[" + str(
            x) + "]" + "/a/span[1]"

        p2 = "//ul[@data-view-name='serverCollection']/li[" + str(
            x) + "]" + "/a/span[2]"

        server.append(
            driver.find_element_by_xpath(p1).text + " " +
            driver.find_element_by_xpath(p2).text)

        link.append(
            "//ul[@data-view-name='serverCollection']/li[" + str(x) + "]")

        ser_link[server[x - 1]] = link[x - 1]

    def click_on_host(server_name, opt=ser_link):
        driver.find_element_by_xpath(ser_link[server_name]).click()

    click_on_host(sys.argv[2])

    # # start the test
    driver.find_element_by_xpath("//*[@class='start-text']").click()

    # wait for the test to be finished
    try:
        WebDriverWait(driver, 120).until(EC.url_contains("result"))
    except Exception as e:
        print(e)

    result = BeautifulSoup(driver.page_source, 'lxml')
    sp = result.find_all('div', class_='result-container-data')[0]

    pi.append(
        sp.find_all('div',
                    class_='result-data u-align-left')[0].text.split('\n')[1])
    dl.append(
        sp.find_all('div',
                    class_='result-data u-align-left')[1].text.split('\n')[1])
    up.append(
        sp.find_all('div',
                    class_='result-data u-align-left')[2].text.split('\n')[1])

    # print(dic)
    driver.close()

c1 = 'PING ms'
c2 = 'DOWNLOAD Mbps'
c3 = 'UPLOAD Mbps'

df = pd.DataFrame({c1: pi, c2: dl, c3: up})
df.index += 1
print(tabulate(df, headers='keys', tablefmt='psql'))
