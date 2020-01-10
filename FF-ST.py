import time
import platform
from datetime import datetime
from xlwt import Workbook
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


##############
# driver = webdriver.Firefox()
# driver.get("https://www.speedtest.net")
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='_evidon-banner-cookiebutton']").click()
# driver.find_element_by_xpath("//*[@id='_evidon-l3']/button").click()
# driver.close()
###############
# while counter < 101:
#     driver = webdriver.Firefox()
#     driver.get("https://www.speedtest.net")
#     driver.get("https://www.speedtest.net")
#     # time.sleep(1)
#     driver.find_element_by_xpath("//*[@id='_evidon-banner-cookiebutton']").click()
#     driver.find_element_by_xpath("//*[@id='_evidon-l3']/button").click()
#     time.sleep(5)
#
#     CorSer = driver.find_element_by_xpath("//div[@data-view-name='currentServer']/div[2]/a")
#     CorLoc = driver.find_element_by_xpath("//div[@data-view-name='currentServer']/div[3]/span")
#
#     if CorSer.text == 'Fastweb SpA' and CorLoc.text == 'Milan':
#         counter += 1
#         time.sleep(1)
#         driver.find_element_by_xpath("//div[@class='privacy-update']/a[2]").click()
#
#         driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div[3]/div[1]/div[1]/a/span[4]").click()
#         #driver.find_element_by_xpath("//a[@class ='js-start-test test-mode-multi']/span[4]").click()
#         #driver.find_element_by_xpath("//a[@href='#' and @role='button']").click()
#         #driver.find_elements_by_css_selector('a.js-start-test.test-mode-multi').click()
#         time.sleep(50)
#         driver.get("https://www.speedtest.net/results")
#         driver.find_element_by_xpath("//*[@id='_evidon-banner-cookiebutton']").click()
#         driver.find_element_by_xpath("//*[@id='_evidon-l3']/button").click()
#
#         DT = datetime.now()
#         DT = DT.strftime('%m/%d/%Y ') + DT.strftime('%I:%M %p')
#
#         PI = driver.find_element_by_xpath("//td[@class='table-number ping-speed' and div[@class='table-major']]")
#
#         DL = driver.find_element_by_xpath("//td[@class='table-number download-speed' and div[@class='table-major']]")
#         UP = driver.find_element_by_xpath("//td[@class='table-number upload-speed' and div[@class='table-major']]")
#         lo = driver.find_element_by_xpath("//td[@class='host-info' and div[@class='table-major']]")
#         LO = str(lo.text).replace("\n", "\t")
#         f.write(str(counter) + '\t' + DT + '\t' + PI.text + '\t' + DL.text + '\t' + UP.text + '\t' + LO + '\n')
#         print  (str(counter) + '\t' + DT + '\t' + PI.text + '\t' + DL.text + '\t' + UP.text + '\t' + LO + '\n')
#         sheet1.write(counter, 0, counter)
#         sheet1.write(counter, 1, DT)
#         sheet1.write(counter, 2, int(PI.text))
#         sheet1.write(counter, 3, DL.text)
#         sheet1.write(counter, 4, UP.text)
#         LO = LO.replace("\t", " ")
#         sheet1.write(counter, 5, LO)
#         if str(platform.system()) == 'Darwin':
#             OS = 'MAC'
#         else:
#             OS = platform.system()
#         sheet1.write(counter, 6, OS)
#         sheet1.write(counter, 7, 'Firefox')
#         sheet1.write(counter, 8, 'Public')
#         sheet1.write(counter, 9, 'Wire')
#         wb.save('FF-ST.xls')
#         # time.sleep(2)
#         driver.close()
#     else:
#         # element = driver.find_element_by_css_selector(
#         #     'div.pure-u-5-12:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > a:nth-child(1)')
#         # element.click()
#         # server = driver.find_element_by_xpath("//*[@id='find-servers']  //a[@data-server-id='7839']").click()
#         # driver.find_element_by_xpath("//*[@id='container']/div[2]/div/div/div/div[3]/div[1]/div[1]/a/span[4]").click()
#         # counter = counter + 1
#         # wait = WebDriverWait(driver, 50)
#         # WebDriverWait(driver, 45).until(EC.url_contains("result"))
#         #
#         # DT = datetime.now()
#         # DT = DT.strftime('%m/%d/%Y ') + DT.strftime('%I:%M %p')
#         #
#         # PI = driver.find_element_by_css_selector(
#         #     "div[title='Reaction Time'] div.result-data.u-align-left>span").get_attribute("innerHTML")
#         # DL = driver.find_element_by_css_selector(
#         #     "div[title='Receiving Time'] div.result-data.u-align-left>span").get_attribute("innerHTML")
#         # UP = driver.find_element_by_css_selector(
#         #     "div[title='Sending Time'] div.result-data.u-align-left>span").get_attribute("innerHTML")
#         # LO = driver.find_element_by_css_selector("div[class='server-current'] div.result-data>span").get_attribute(
#         #     "innerHTML")
#         # SE = driver.find_element_by_css_selector("div[class='server-current'] div.result-label>a").get_attribute(
#         #     "innerHTML")
#         #
#         # f.write(str(counter) + '\t' + DT + '\t' + PI + '\t' + DL + '\t' + UP + '\t' + LO + '\t' + SE + '\n')
#         # print  (str(counter) + '\t' + DT + '\t' + PI + '\t' + DL + '\t' + UP + '\t' + LO + '\t' + SE + '\n')
#         # sheet1.write(counter, 0, int(counter))
#         # sheet1.write(counter, 1, DT)
#         # sheet1.write(counter, 2, int(PI))
#         # sheet1.write(counter, 3, DL)
#         # sheet1.write(counter, 4, UP)
#         # sheet1.write(counter, 5, LO + ' ' + SE)
#         # if str(platform.system()) == 'Darwin':
#         #     OS = 'MAC'
#         # else:
#         #     OS = platform.system()
#         # sheet1.write(counter, 6, OS)
#         # sheet1.write(counter, 7, 'Firefox')
#         # sheet1.write(counter, 8, 'Public')
#         # wb.save('FF-ST1.xls')
#         # time.sleep(2)
#         driver.close()
#
#
