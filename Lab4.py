import requests
from bs4 import BeautifulSoup
from queue import Queue
import threading
import time

def getting_posts(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all('div', {'data-adaptive': '1'})

    posts = []

    for item in items:
        try:
            date = item.find('span', {'class':'name'}).get('title')
        except AttributeError:
            content = ''
        try:
            author = item.find('p', {'class': 'name'}).text
        except AttributeError:
            author = ''
        try:
            title = item.find('div', {'class':'caption'}).find('h3').text
        except AttributeError:
            title = ''
        try:
            subtitle = item.find('p', {'class':'subtitle'}).text
        except AttributeError:
            subtitle = ''
        try:
            anounce = item.find('div', {'class':'lead'}).find('p').text
        except AttributeError:
            anounce = ''

        posts.append({'date': date,
                   'author': author,
                   'title': title,
                    'subtitle': subtitle,
                   'anounce': anounce})

    return posts
    time.sleep(300)



url = 'https://nplus1.ru/'
posts = getting_posts(url)

queue = Queue()
thread = threading.Thread(target=getting_posts, args=(url, queue))
thread.start()
while True:
    news = queue.get()
if news['date'] != '':
    print(news['date'])
if news['author'] != '':
    print(news['author'])
if news['title'] != '':
    print(news['title'])
if news['subtitle']!='':
    print(news['subtitle'])
if news['anounce'] != '':
    print(news['anounce'])
print('\n')