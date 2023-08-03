import argparse

def config_flags():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-u", "--username", dest = "username", help="Login name", required=True, type=str)
    parser.add_argument("-p", "--password",dest = "password", help="Password", required=True, type=str)
    parser.add_argument("-t", "--topic", dest = "topic", help="Topic", required=True, type=str)

    args = parser.parse_args()

    return args

config = config_flags()

CHROME_PATH = ".\chromedriver\chromedriver_win32\chromedriver"
EDGE_PATH = ".\chromedriver\edgedriver_win64\msedgedriver.exe"
DELAY = 5 #seconds
CONFIG = config
MAXWORD = 10**6
POST_LENGTH = 100