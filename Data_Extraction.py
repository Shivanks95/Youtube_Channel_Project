from selenium import webdriver
from bs4 import BeautifulSoup
import json

urls =[
    'krishnaik06'
]

def watch():
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/user/{}/videos?view=0&sort=dd&flow=grid'.format(urls[0]))
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    titles = soup.find_all('a', id='video-title')
    player_urls = soup.find_all('a',id='video-title')

    for title in titles[:10]:
        i = 0
        return "\thttps://www.youtube.com{}".format(player_urls[i].get('href'))
        i+=1
def likes_comments():
    driver = webdriver.Chrome()
    driver.get(watch())
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')
    likes= soup.find_all('yt-formatted-string', id='text')

    for like in likes:
        print(like.text)

watch()
likes_comments()