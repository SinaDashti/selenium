import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tabulate import tabulate
import pandas as pd
from bs4 import BeautifulSoup
import sys
import argparse


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def banner_click(self, clickBanner, closeBanner, optionBanner):

        try:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(clickBanner)).click()

            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(closeBanner)).click()

        except Exception as e:
            try:
                WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable(optionBanner)).click()
            except Exception as e:
                print("The banner does not allow continue!\n")



class ServerSelection():
    def __init__(self, driver):

        self.driver = driver
        self.server = []
        self.link = []
        self.ser_link = {}

    def server_select(self,
                      serverElement,
                      serverList,
                      serverStr,
                      serverSelect=None):
        # choosing server
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(serverElement)).click()

        li = self.driver.find_elements_by_xpath(serverList)

        for x in range(1, (len(li) + 1)):

            p1 = serverStr + str(x) + "]/a/span[1]"
            p2 = serverStr + str(x) + "]/a/span[2]"

            self.server.append(
                self.driver.find_element_by_xpath(p1).text + " " +
                self.driver.find_element_by_xpath(p2).text)

            self.link.append(serverStr + str(x) + "]")

            self.ser_link[self.server[x - 1]] = self.link[x - 1]

        if serverSelect == None:
            serverSelect = self.server[0]
        # def click_on_host(server_name, opt = self.ser_link):
        #     self.driver.find_element_by_xpath(self.ser_link[server_name]).click()
        #
        # click_on_host(serverSelect)
        self.driver.find_element_by_xpath(self.ser_link[serverSelect]).click()


class StartSpeedTest():
    def __init__(self, driver):
        self.driver = driver

    def start_click(self, clickStart):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(clickStart)).click()


class WaitForResult():
    def __init__(self, driver):
        self.driver = driver

    def url_wait(self, urlContain):
        try:
            WebDriverWait(self.driver, 120).until(EC.url_contains(urlContain))
        except Exception as e:
            print(e)


class ResultExtract():
    def __init__(self, driver):

        self.driver = driver

    def save_result(self, resultAttribute, valueAttribute):

        result = BeautifulSoup(self.driver.page_source, 'lxml')
        sp = result.find_all('div', class_=resultAttribute)[0]

        self.pi = sp.find_all(
            'div', class_=valueAttribute)[0].text.split('\n')[1]
        self.dl = sp.find_all(
            'div', class_=valueAttribute)[1].text.split('\n')[1]
        self.up = sp.find_all(
            'div', class_=valueAttribute)[2].text.split('\n')[1]

        return self.pi, self.dl, self.up


class ShowResult():
    def show_result(self, ping, download, upload):

        c1 = 'PING ms'
        c2 = 'DOWNLOAD Mbps'
        c3 = 'UPLOAD Mbps'

        df = pd.DataFrame({c1: ping, c2: download, c3: upload})
        df.index += 1
        print(tabulate(df, headers='keys', tablefmt='psql'))
