from Locators import Locators
from other.TestData import TestData
from extra.NewExtra.extra import BasePage, StartSpeedTest, WaitForResult, ResultExtract, ShowResult, ServerSelection
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tabulate import tabulate
from bs4 import BeautifulSoup
import pandas as pd
import unittest
import sys
import argparse


class OoklaSpeedTest(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.get(TestData.BASE_URL)
        self.ping = []
        self.download = []
        self.upload = []

    def runTest(self):
        def test_cycle():

            banner = BasePage(self.driver)
            banner.banner_click(Locators.CLICK_BANNER, Locators.CLOSE_BANNER,
                                Locators.OPTION_BANNER)

            server = ServerSelection(self.driver)
            server.server_select(Locators.SERVER_ELEMENT, Locators.SERVER_LIST,
                                 Locators.SERVER_STR, TestData.SERVER_CHOICE)

            start = StartSpeedTest(self.driver)
            start.start_click(Locators.START_BUTTON)

            wait = WaitForResult(self.driver)
            wait.url_wait(Locators.URL_CONTAIN)

            result = ResultExtract(self.driver)
            out = result.save_result(Locators.RESULT_ATTRIBUTE,
                                     Locators.VALUE_ATTRIBUTE)

            self.ping.append(out[0])
            self.download.append(out[1])
            self.upload.append(out[2])

        if TestData.ARGS_INPUT >= 2:

            for i in range(int(TestData.REPEAT_NUMBER)):
                test_cycle()
                if i < (int(TestData.REPEAT_NUMBER) - 1):
                    self.driver.get(TestData.BASE_URL)

        else:
            test_cycle()

        show = ShowResult()
        show.show_result(self.ping, self.download, self.upload)

    def tearDown(self):
        self.driver.close()


# if __name__ == "__main__":
#     unittest.main()

unittest.TextTestRunner().run(OoklaSpeedTest())
