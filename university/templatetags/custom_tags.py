from django import template

from lxml import html

import requests

from random import randint

register = template.Library()

@register.filter
def modify_name(value, arg):
    pass

@register.simple_tag
def random_quote():
    url = f'https://quotes.toscrape.com/page/{randint(1,11)}/'
    r = requests.get(url)
    tree = html.fromstring(r.text)
    quote = tree.xpath('//span[@class = "text"]')
    author = tree.xpath('//small[@class = "author"]')

    number = randint(0,9)

    return f'{author[number].text}: {quote[number].text}'

