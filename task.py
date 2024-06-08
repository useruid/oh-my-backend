from urllib.parse import urlparse
from hashlib import md5
import random

GLOBAL_URL_STORAGE = {}

BASE_URL = "https://xxx.com"
URL_GEN_BASE = [1, 2, 3, 4, 5, 6, 7, 10, 'a', 'b', 'c', 'd', 'e', 'f', 'g']


def generate_short_url(length: int) -> str:
    res = ''.join([str(i) for i in random.choices(URL_GEN_BASE, k=length)])
    return res


if __name__ == '__main__':

    # creating
    to_shorten = "https://www.google.com"
    generated_url = generate_short_url(5)
    output = BASE_URL + '/' + generated_url
    GLOBAL_URL_STORAGE[output] = to_shorten
    print(output)

    # redirect
    shorten_url = output
    redirect_to = GLOBAL_URL_STORAGE[shorten_url]


a = [1, 2, 3]

a * 2

a.extend(a)

a.extend([*a])

test_dct = {'test': 1}

from functools import reduce

filter()
map
filter

reduce(lambda x, y: x + y, [1, 2, 3])
