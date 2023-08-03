import threading

from configs.config import MAXWORD as max_length
from logics.logics import push_to_archive


def handle_data(ch, archive, done):
    count_word = 0
    
    while count_word <= max_length and not done.is_set():
        if len(ch) > 0:
            string = ch.pop(0)
            count_word += len(string)
            print(count_word)
            push_to_archive(string, archive)
    done.set()
