from selenium.webdriver.common.by import By


class Locators():

    CLICK_BANNER = (By.XPATH, "//*[@id='_evidon-banner-cookiebutton']")
    CLOSE_BANNER = (By.XPATH, "//*[@id='_evidon-l3']/button")
    OPTION_BANNER = (By.XPATH, "//*[@id='_ev_opt_out_close']")
    ACCEPT_BANNER = (By.XPATH, "//*[@id='_evidon-banner-acceptbutton']/button")
    LOAD_PAGE = (By.XPATH, "//div[@data-view-name='currentServer']/div[2]/a")
    START_BUTTON = (By.XPATH, "//*[@class='start-text']")
    CLOSE_BUTTON = (By.CLASS_NAME, "ui-dialog-buttonset")
    SERVER_ELEMENT = (By.XPATH, "//div[@class='result-data'][2]/child::a[1]")
    SERVER_LIST = "//ul[@data-view-name='serverCollection']/li"
    SERVER_STR = "//ul[@data-view-name='serverCollection']/li["
    VALUE_ATTRIBUTE = 'result-data u-align-left'
    RESULT_ATTRIBUTE = 'result-container-data'
    URL_CONTAIN = "result"
