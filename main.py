from collections import Counter, defaultdict
import threading

from selenium import webdriver
import sys
from os.path import dirname, abspath

# Get the absolute path of the parent directory (project root)
project_root = abspath(dirname(dirname(__file__)))

# Add the parent directory to the Python path
sys.path.insert(0, project_root)

from configs.config import CHROME_PATH
from configs.config import POST_LENGTH as length
from threads.twitter_thread import twitter_data
from threads.reddit_thread import reddit_data
from threads.handle_data import handle_data
from logics.logics import prepare_post
from threads.time_out import timeout


if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    twitter_driver = webdriver.Chrome(CHROME_PATH, chrome_options=chrome_options)
    twitter_driver.implicitly_wait(10)

    reddit_driver = webdriver.Chrome(CHROME_PATH, chrome_options=chrome_options)
    reddit_driver.implicitly_wait(10)
    
    dataCollector = defaultdict(Counter)
    stop_flag = threading.Event()
    chanel = []

    twitter_thread = threading.Thread(target=twitter_data, args=(twitter_driver, chanel, stop_flag))
    reddit_thread = threading.Thread(target=reddit_data, args=(reddit_driver, chanel, stop_flag))
    handle_thread = threading.Thread(target=handle_data, args=(chanel, dataCollector, stop_flag))
    timeout_thread = threading.Thread(target=timeout, args=(stop_flag,))

    twitter_thread.start()
    reddit_thread.start()
    handle_thread.start()
    timeout_thread.start()

    twitter_thread.join()
    reddit_thread.join()
    handle_thread.join()

    print(prepare_post(dataCollector, length))
