import time

from configs.config import MAXWORD as le

def timeout(time_up):
    cou = 0
    while cou < 100 and not time_up.is_set():
        time.sleep(1)
        cou += 1
    print("time is up!!!!!")
    time_up.set()