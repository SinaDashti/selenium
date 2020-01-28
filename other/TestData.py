import sys


class TestData():

    # Example of path for windows
    # P = "C:\\Users\\SinaDashti\\Desktop\\pageobject\\Drivers\\geckodriver.exe"
    # FIREFOX_EXECUTABLE_PATH = P
    BASE_URL = "https://www.speedtest.net"

    if len(sys.argv) == 1:
        ARGS_INPUT = 0
        REPEAT_NUMBER = 1
        SERVER_CHOICE = None

    elif len(sys.argv) == 2:
        ARGS_INPUT = 1
        REPEAT_NUMBER = sys.argv[1]
        SERVER_CHOICE = None

    elif len(sys.argv) == 3:
        ARGS_INPUT = len(sys.argv)
        REPEAT_NUMBER = sys.argv[1]
        SERVER_CHOICE = sys.argv[2]
