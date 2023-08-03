from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logics.logics import handle_post_twitter
from configs.config import DELAY as delay, CONFIG as config


def twitter_data(dri, ch, done):
    dri.get("https://twitter.com/i/flow/login")
    dri.maximize_window()

    try:
        username_input_box = WebDriverWait(dri, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")))
        print("found username!")
    except TimeoutException:
        print("Loading username took too much time!")

    print(username_input_box.get_attribute('name'))
    username_input_box.clear()
    username_input_box.send_keys(config.username, Keys.ENTER)

    try:
        password_input_box = WebDriverWait(dri, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        print("found pass!")
    except TimeoutException:
        print("Loading pass took too much time!")

    password_input_box.clear()
    password_input_box.send_keys(config.password, Keys.ENTER)

    if "enter your password" in dri.page_source.lower():
        print("wrong password!")

    try:
        search_box = WebDriverWait(dri, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")))
        print("found search on twitter!")
    except TimeoutException:
        print("Loading search on twitter took too much time!")

    search_box.clear()
    search_box.send_keys(config.topic, Keys.ENTER)

    while not done.is_set():
        try:
            posts = WebDriverWait(dri, delay).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div/div/div/div/div/article/div/div/div[2]/div[2]/div[2]/div/span")))
            print("found post on twitter!")
        except TimeoutException:
            print("Loading post on twitter took too much time!")

        handle_post_twitter(dri, posts, ch)
        dri.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    dri.quit()


