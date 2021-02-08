import re
from random import randint

from django import template

from lxml import html

import redis

import requests


red = redis.Redis()

register = template.Library()


@register.filter
def modify_string(value):
    '''
    if red.get("0"):
        word_list = []
        for i in range(10):
            word_list += red.get(str(i))[2:-1]

    url = f'https://random-word-api.herokuapp.com/word?number=10'
    r = requests.get(url)
    word_list = r.text
    '''
    word_list = [
        "reoxidize", "cutinizes", "vibes", "melodeons", "paranoid", "busticated",
        "disremembers", "camelias", "lipotropy", "tallest", "chalcopyrite", "designative",
        "stereochemistry", "outlearning", "subseres", "armor", "briards", "factored",
        "lovebirds", "pirayas", "crankle", "eudiometric", "haziness", "fauve", "subatomic",
        "dryades", "browns", "academisms", "italianates", "wimpishness", "pemican",
        "dispersive", "reflag", "plesiosaur", "atheromas", "funnelling", "exaptive",
        "slashers", "unmanlinesses", "vills", "pelletize", "declarants", "inflight",
        "timberwork", "zoeae", "repave", "italianises", "updos", "cloy", "squawkers", "Aaron"
    ]

    for word in word_list:
        rep = "*" * len(word)
        value = re.sub(r'\b' + re.escape(word) + r'\b', rep, value)

    '''
    for num, word in enumerate(word_list):
        red.set(str(num), word)
        red.expire(str(num), 5)

    for word in word_list:
        rep = '*' * len(word)
        result = value.replace(word, rep)
        value = result
    '''
    return value


@register.simple_tag
def random_quote():
    url = f'https://quotes.toscrape.com/page/{randint(1, 10)}/'
    r = requests.get(url)
    tree = html.fromstring(r.text)
    quote = tree.xpath('//span[@class = "text"]')
    author = tree.xpath('//small[@class = "author"]')

    number = randint(0, 9)

    return f'{author[number].text}: {quote[number].text}'
