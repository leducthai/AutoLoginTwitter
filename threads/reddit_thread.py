import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logics.logics import handle_post_reddit
from configs.config import DELAY as delay, CONFIG as config

def reddit_data(dri, ch, done):

    dri.get(f"https://www.reddit.com/search/?q={config.topic}")
    dri.maximize_window()

    while not done.is_set():
        try:
            posts = WebDriverWait(dri, delay).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='search-results-tab-slot']/reddit-feed/faceplate-tracker//a")))
            print("found post on reddit!")
        except TimeoutException:
            print("Loading post on reddit took too much time!")
        
        handle_post_reddit(posts, ch)
        dri.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    dri.quit()
