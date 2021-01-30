# Create your tasks here
from celery import shared_task

from django.core.mail import send_mail as django_send_mail

from .models import Author, Quote

import requests
from bs4 import BeautifulSoup
from lxml import html, etree
import re

import unicodedata


@shared_task
def send_mail(subject, message, from_email):
    django_send_mail(subject, message, from_email, ['admin@example.com'])


@shared_task
def add_quote():
    url = 'https://quotes.toscrape.com/page/{number}/'
    q_count = Quote.objects.count()

    if q_count == 100:
        django_send_mail('Quotes', 'No quotes', 'ex@ex.com', ['admin@example.com'])
        
    else:
        a_list = Author.objects.all()
        print(q_count)
        i = q_count // 10

        add_count = 1
        while i <= 10:
            url_page = url.format(number=i)
            r = requests.get(url_page)
            tree = html.fromstring(r.text)

            quote = tree.xpath('//span[@class = "text"]')
            name = tree.xpath('//small[@class = "author"]')
            tags = tree.xpath('//meta[@class = "keywords"]')
            hrefs = tree.xpath('//a[text() = "(about)"]')


            counter = q_count % 10 - 1
            while counter < 10:
                authors_link = f'https://quotes.toscrape.com{hrefs[counter].attrib["href"]}/'

                author_r = requests.get(authors_link)
                tree = html.fromstring(author_r.text)

                born_date = tree.xpath('//span[@class = "author-born-date"]')
                born_location = tree.xpath('//span[@class = "author-born-location"]')
                description = tree.xpath('//div[@class = "author-description"]')

                for author_for in range (Author.objects.count()):
                    if author_for.name == name[counter].text:
                        authorr = Author.objects.get(name=name[counter].text)

                else:
                    authorr = Author.objects.create(

                        name = name[counter].text,
                        date_of_birth = born_date[0].text,
                        born_location = born_location[0].text,
                        about = description[0].text,


                    )

                Quote.objects.create(
                    quote = quote[counter].text, 
                    tags = tags[counter].attrib['content'].replace(',', ', '), 
                    author = authorr
                )
                if add_count == 5:
                    return
                add_count += 1
                counter += 1
            
            i += 1
