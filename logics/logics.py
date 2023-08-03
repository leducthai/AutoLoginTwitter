from random import choice

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def handle_post_twitter(dri, posts, ch):
    for post in posts:
        try:
            post = WebDriverWait(dri, 3).until(EC.visibility_of(post))
            contents = post.text
        except: 
            continue
        if len(contents) > 0: 
            ch.append(contents)

def handle_post_reddit(posts, ch):
    for post in posts:
        contents = post.text
        if len(contents) > 0: 
            ch.append(contents)

def push_to_archive(string:str, archive):
    words = string.split()
    for i in range(len(words) - 1):
        archive[words[i]][words[i + 1]] += 1

def prepare_post (archive, length):
    ar = list(archive.keys())
    if len(ar) == 0 :
        return "empty archive"
    cur = get_random_word(ar)
    newpost = cur
    for _ in range(length - 1):
        nxt = next_word(cur, archive)
        if len(nxt) <= 0 :
            cur = get_random_word(ar)
            newpost += ". " + cur
            continue
        eliminate_word(cur, nxt[0][0], archive)
        cur = nxt[0][0]
        newpost += " " + cur

    return newpost

def get_random_word(poll):
    return choice(poll)

def next_word(cur, archive):
    return archive[cur].most_common(1)

def eliminate_word(k, v, archive):
    archive[k][v] = 0