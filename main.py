import time
from selenium import webdriver
from config import config_flags
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

config = config_flags()

CHROME_PATH = ".\chromedriver\chromedriver_win32\chromedriver"
EDGE_PATH = ".\chromedriver\edgedriver_win64\msedgedriver.exe"
delay = 3 #seconds
# create webdriver object
driver = webdriver.Chrome(CHROME_PATH)
driver.implicitly_wait(10)


driver.get("https://twitter.com/login")
driver.maximize_window()

try:
    username_input_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!"
)
print(username_input_box.get_attribute('name'))
username_input_box.clear()
username_input_box.send_keys(config.username, Keys.ENTER)

try:
    password_input_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!"
)
password_input_box.clear()
password_input_box.send_keys(config.password, Keys.ENTER)

if "enter your password" in driver.page_source.lower():
    print("wrong password!")

try:
    search_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

search_box.clear()
search_box.send_keys(config.topic, Keys.ENTER)

driver.set_window_size(2300, 1080)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)



